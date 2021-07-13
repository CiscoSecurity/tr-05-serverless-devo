import json
import time
import requests

from flask import current_app
from json import JSONDecodeError
from api.errors import DevoError, DevoSSLError
from devo.api.client import raise_exception, ERROR_MSGS

from devo.api import (
    Client,
    DevoClientException,
    ClientConfig,
    JSON_SIMPLE
)


ERRORS = {
    "no_endpoint": "Host not found",
    "no_respond": ("Devo didn't respond in time. "
                   "Please, check your key/secret or auth token/jwt")
}
ERROR_MSGS.update(ERRORS)
ERROR_MSGS['no_auth'] = "Client doesn't have key&secret or auth token/jwt"


def handle_devo_errors(func):
    def wraps(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.SSLError as error:
            raise DevoSSLError(error)
        except DevoClientException as error:
            try:
                raise DevoError(error.args[0]['object'])
            except KeyError:
                raise DevoError(error.args[0]['error']['message'])
            except TypeError:
                raise DevoError(json.loads(error.args[0])['object'])
        except (ConnectionError, requests.exceptions.ConnectionError) as error:
            raise DevoError(error.args[0].args[0])
        except JSONDecodeError:
            return []
        except requests.exceptions.InvalidHeader as error:
            raise DevoError(error.args[0])

    return wraps


class DevoClient(Client):
    def __init__(self, credentials):
        self.credentials = credentials
        self.config = ClientConfig(
            response="json/simple",
            processor=JSON_SIMPLE,
            stream=True
        )
        timeout = current_app.config['DEFAULT_TIMEOUT']
        retries = current_app.config['DEFAULT_RETRIES']
        self.default_limit = current_app.config['DEFAULT_CTR_ENTITIES_LIMIT']
        super().__init__(auth=self._auth, address=self._address,
                         retries=retries, config=self.config, timeout=timeout)

    @property
    def _auth(self):
        return {
            "key": self.credentials['KEY'],
            "secret": self.credentials['SECRET']
        }

    @property
    def _address(self):
        host = self.credentials['HOST']
        if not host:
            raise DevoError(ERROR_MSGS['no_endpoint'])
        return host

    @property
    def limit(self):
        try:
            limit = int(self.credentials['CTR_ENTITIES_LIMIT'])
            assert limit <= self.default_limit
        except (ValueError, KeyError, AssertionError):
            return self.default_limit
        return limit

    def _get_headers(self, data):
        headers = super(DevoClient, self)._get_headers(data)
        headers['User-Agent'] = current_app.config['USER_AGENT']
        return headers

    @handle_devo_errors
    def search(self, observable, limit=None):
        """
        Query API by a custom query
        :param observable: observable value which need to be investigated
        :param limit: max number of rows
        :return: list
        """
        if limit is None:
            limit = self.limit
        response = self.query(
            query=f"from all.data where toktains(message, '{observable}')",
            dates={
                "from": "now()-30*day()",
                "to": "now()"
            },
            limit=limit + 1
        )

        return [data for data in response]

    def _call_jobs(self, address):
        """
        Make the call
        :param address: endpoint
        :return: Response from API
        """
        tries = 0
        while tries < self.retries:
            response = None
            try:
                response = requests.get("https://{}".format(address),
                                        headers=self._get_headers(""),
                                        verify=self.verify,
                                        timeout=self.timeout)
            except ConnectionError as error:
                raise_exception({"status": 404, "msg": error})

            if response:
                if response.status_code != 200 or\
                        "error" in response.text[0:15].lower():
                    raise_exception(response.text)
                    return None
                try:
                    return json.loads(response.text)
                except json.decoder.JSONDecodeError:
                    return response.text
            tries += 1
            time.sleep(self.timeout)
        raise raise_exception({
            "status": 400,
            "object": ERROR_MSGS['no_respond']
        })

    @handle_devo_errors
    def get_jobs(self, job_type=None, name=None):
        return super(DevoClient, self).get_jobs(job_type, name)
