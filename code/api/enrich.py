from flask import Blueprint, g
from functools import partial
from api.mapping import Mapping
from api.client import DevoClient
from api.schemas import ObservableSchema
from api.errors import TooManyMessagesWarning

from api.utils import (
    get_json,
    get_credentials,
    jsonify_data,
    filter_observables,
    jsonify_result,
    add_error
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
    mapping = Mapping()

    for observable in observables:
        messages = client.query(observable['value'])
        for msg in messages:

            sighting = mapping.extract_sighting(observable, msg)
            g.sightings.append(sighting)
        if len(messages) >= client.default_limit:
            add_error(TooManyMessagesWarning(observable['value']))
    return jsonify_result()


@enrich_api.route('/refer/observables', methods=['POST'])
def refer_observables():
    _ = get_credentials()
    _ = get_observables()
    return jsonify_data([])
