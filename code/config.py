import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings["VERSION"]

    SUPPORTED_TYPES = {
        'ip': 'IP'
    }
    API_URL = 'https://{host}/search/query'

    DEFAULT_CTR_ENTITIES_LIMIT = 100
    TOO_MANY_MSGS_WARNING_LIMIT = DEFAULT_CTR_ENTITIES_LIMIT + 1

    USER_AGENT = ('SecureX Threat Response Integrations '
                  '<tr-integrations-support@cisco.com>')
