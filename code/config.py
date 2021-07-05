import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings["VERSION"]

    SUPPORTED_TYPES = {
        'ip': 'IP'
    }
    API_URL = 'https://{host}/search/query'
