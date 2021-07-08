from flask import current_app
from json import JSONDecodeError
from api.errors import DevoError, DevoSSLError
from requests.exceptions import ConnectionError, SSLError

from devo.api import (
    Client,
    DevoClientException,
    ClientConfig,
    JSON_SIMPLE
)

ERROR_MSGS = {
    "no_endpoint": "Host not found"
}


def handle_devo_errors(func):
    def wraps(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SSLError as error:
            raise DevoSSLError(error)
        except DevoClientException as error:
            try:
                raise DevoError(error.args[0]['object'])
            except KeyError:
                raise DevoError(error.args[0]['error']['message'])
        except ConnectionError as error:
            raise DevoError(error.args[0].args[0])
        except JSONDecodeError:
            return []

    return wraps


class DevoClient(Client):
    def __init__(self, credentials):
        self.credentials = credentials
        self.config = ClientConfig(
            response="json/simple",
            processor=JSON_SIMPLE,
            stream=True
        )
        self.default_limit = current_app.config['DEFAULT_CTR_ENTITIES_LIMIT']
        super().__init__(auth=self._auth, address=self._address,
                         retries=2, config=self.config)

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
