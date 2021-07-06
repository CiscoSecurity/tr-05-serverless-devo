from flask import current_app
from api.errors import DevoError
from devo.api import Client, DevoClientException
from requests.exceptions import ConnectionError

ERROR_MSGS = {
    "no_endpoint": "Host not found"
}


def handle_devo_errors(func):
    def wraps(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DevoClientException as error:
            try:
                raise DevoError(error.args[0]['object'])
            except KeyError:
                raise DevoError(error.args[0]['error']['message'])
        except ConnectionError as error:
            raise DevoError(error.args[0].args[0])
    return wraps


class DevoClient:
    def __init__(self, credentials):
        self.credentials = credentials
        self._client = self._authorize(self._auth, self._address)
        self.default_limit = current_app.config['DEFAULT_CTR_ENTITIES_LIMIT']

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
        return current_app.config['API_URL'].format(
            host=self.credentials['HOST'])

    @property
    def limit(self):
        try:
            limit = int(self.credentials['CTR_ENTITIES_LIMIT'])
        except (ValueError, KeyError):
            return self.default_limit
        return limit

    @staticmethod
    def _authorize(auth, address, retries=2):
        """
        Authorize on specific address with given credentials in auth
        :param auth: object which contains params (key, secret)
        :param address: endpoint
        :param retries: number of retries for a query
        :return: <class 'devo.api.client.Client'>
        """
        return Client(auth=auth, address=address, retries=retries)

    @handle_devo_errors
    def query(self, observable, limit=None):
        """
        Query API by a custom query
        :param observable: observable value which need to be investigated
        :param limit: max number of rows
        :return: list
        """
        if limit is None:
            limit = self.limit
        response = self._client.query(
            query=f"from all.data where toktains(message, '{observable}')",
            dates={
                "from": "now()-30*day()",
                "to": "now()"
            },
            limit=limit
        )

        return [data for data in response]

    @handle_devo_errors
    def jobs(self, type_=None, name=None):
        """
        Get list of jobs by type and name, default All
        :param type_: category of jobs
        :param name: name of jobs
        :return: json
        """

        return self._client.get_jobs(type_, name)
