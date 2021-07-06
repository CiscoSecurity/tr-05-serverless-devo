from flask import Blueprint, g
from functools import partial
from api.client import DevoClient
from api.schemas import ObservableSchema

from api.utils import (
    get_json,
    get_credentials,
    jsonify_data,
    filter_observables
)

enrich_api = Blueprint('enrich', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/deliberate/observables', methods=['POST'])
def deliberate_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data({})


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    credentials = get_credentials()
    observables = filter_observables(get_observables())

    g.sightings = []

    client = DevoClient(credentials)
    for observable in observables:
        _ = client.query(observable['value'])

    return jsonify_data({})


@enrich_api.route('/refer/observables', methods=['POST'])
def refer_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data([])
