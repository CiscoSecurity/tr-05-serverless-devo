from functools import partial
from api.mapping import Mapping
from api.client import DevoClient
from api.schemas import ObservableSchema
from flask import Blueprint, g, current_app
from api.errors import TooManyMessagesWarning

from api.utils import (
    get_json,
    get_credentials,
    filter_observables,
    jsonify_result,
    add_error
)


enrich_api = Blueprint('enrich', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    credentials = get_credentials()
    observables = filter_observables(get_observables())

    g.sightings = []

    client = DevoClient(credentials)
    mapping = Mapping()

    for observable in observables:
        messages = client.search(observable['value'])
        for msg in messages[:client.limit]:

            sighting = mapping.extract_sighting(observable, msg)
            g.sightings.append(sighting)
        if len(messages) >= current_app.config['TOO_MANY_MSGS_WARNING_LIMIT']:
            add_error(TooManyMessagesWarning(observable['value']))
    return jsonify_result()
