from uuid import uuid5, NAMESPACE_X500
from datetime import datetime, timezone


SIGHTING = 'sighting'
TITLE = (
    'Log message received by '
    'Devo in last 30 days contains observable'
)

SHORT_DESCRIPTION = (
    'Devo received a log message from '
    '{hostname} containing'
    ' the observable')

SIGHTING_DEFAULTS = {
    'title': TITLE,
    'confidence': 'High',
    'count': 1,
    'schema_version': '1.1.6',
    'type': SIGHTING,
    'internal': True,
    'source': 'Devo'
}

DATA = (
    "technology",
    "brand",
    "phylum",
    "family",
    "genus",
    "species"
)


class Mapping:

    @staticmethod
    def _transient_id(type_, title, timestamp, message) -> str:
        seeds = f'{type_}|{title}|{timestamp}|{message}'
        return f'transient:{type_}-{uuid5(NAMESPACE_X500, seeds)}'

    @staticmethod
    def _observed_time(msg) -> dict:
        return {
            'start_time': datetime.fromtimestamp(
                msg.get("eventdate") / 1000.0, timezone.utc
            ).isoformat(timespec="milliseconds")
        }

    @staticmethod
    def _table(msg) -> dict:
        data = {"columns": [], "rows": [[]]}

        for key, value in msg.items():
            if key in DATA and value != '':
                data["columns"].append({"name": key, "type": "string"})
                data["rows"][0].append(str(value))

        return data

    def extract_sighting(self, observable, msg) -> dict:
        return {
            'id': self._transient_id(
                SIGHTING, TITLE,
                msg.get("eventdate"),
                msg.get("message")
            ),
            'description': f"```\n{msg.get('message', '')}\n```",
            'observables': [observable],
            'short_description': SHORT_DESCRIPTION.format(
                hostname=msg["hostName"]
            ),
            'observed_time': self._observed_time(msg),
            'data': self._table(msg),
            **SIGHTING_DEFAULTS
        }
