from devo.api import Client
from flask import Blueprint
from flask import current_app
from api.utils import get_jwt, jsonify_data

health_api = Blueprint('health', __name__)


@health_api.route('/health', methods=['POST'])
def health():
    _ = get_jwt()
    client = Client(auth={
        "key": current_app.config['KEY'],
        "secret": current_app.config['SECRET']
    },
        address=current_app.config['API_URL'].format(
            host=current_app.config['HOST'])
    )

    client.get_jobs()

    return jsonify_data({'status': 'ok'})
