from flask import Blueprint
from api.client import DevoClient
from api.utils import get_credentials, jsonify_data

health_api = Blueprint('health', __name__)


@health_api.route('/health', methods=['POST'])
def health():
    credentials = get_credentials()
    client = DevoClient(credentials)
    _ = client.query('1.1.1.1', limit=1)

    return jsonify_data({'status': 'ok'})
