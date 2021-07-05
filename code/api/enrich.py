from flask import Blueprint, g
from functools import partial
from api.client import DevoClient
from api.schemas import ObservableSchema

from api.utils import get_json, get_jwt, jsonify_data, filter_observables

enrich_api = Blueprint('enrich', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))


@enrich_api.route('/deliberate/observables', methods=['POST'])
def deliberate_observables():
    _ = get_jwt()
    _ = get_observables()
    return jsonify_data({})


@enrich_api.route('/observe/observables', methods=['POST'])
def observe_observables():
    _ = get_jwt()
    observables = filter_observables(get_observables())

    g.sightings = []

    client = DevoClient()

    for observable in observables:
        response = client.query(query=f"from all.data where toktains(message, '{observable['value']}')",
                                dates={"from": "2018-02-06 12:42:00", 'to': "now"},
                                limit=101)
        try:
            for item in response:
                print(item)
        except Exception as error:
            print(error)
    return jsonify_data({})


@enrich_api.route('/refer/observables', methods=['POST'])
def refer_observables():
    _ = get_jwt()
    _ = get_observables()
    return jsonify_data([])
