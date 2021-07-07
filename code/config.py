import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings["VERSION"]

    SUPPORTED_TYPES = {
        'ip': 'IP'
    }
    API_URL = 'https://{host}/search/query'

    DEFAULT_CTR_ENTITIES_LIMIT = 100

    USER_AGENT = ('SecureX Threat Response Integrations '
                  '<tr-integrations-support@cisco.com>')
