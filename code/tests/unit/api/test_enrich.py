from pytest import fixture
from http import HTTPStatus

from requests.exceptions import SSLError

from .utils import get_headers
from unittest.mock import patch
from ..conftest import mock_api_response
from ..payloads_for_tests import (
    EXPECTED_RESPONSE_OF_JWKS_ENDPOINT,
    base_payload,
    EXPECTED_RESPONSE_FROM_DEVO
)


def routes():
    yield '/observe/observables'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


@fixture(scope='module')
def invalid_json_value():
    return [{'type': 'ip', 'value': ''}]


@patch('requests.get')
def test_enrich_call_with_valid_jwt_but_invalid_json_value(
        mock_request,
        route, client, valid_jwt, invalid_json_value,
        invalid_json_expected_payload
):
    mock_request.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    response = client.post(route,
                           headers=get_headers(valid_jwt()),
                           json=invalid_json_value)
    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_json_expected_payload(
        "{0: {'value': ['Field may not be blank.']}}"
    )


@fixture(scope='module')
def valid_json():
    return [{'type': 'ip', 'value': '27.123.176.106'}]


@patch('api.client.DevoClient.query')
@patch('requests.get')
def test_enrich_call_success(mock_request, mock_response,
                             route, client, valid_jwt, valid_json):
    mock_response.side_effect = [EXPECTED_RESPONSE_FROM_DEVO]
    mock_request.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    response = client.post(route, headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == base_payload()


@patch('devo.api.Client.query')
@patch('requests.get')
def test_enrich_call_with_ssl_error(mock_get, mock_request,
                                    mock_exception_for_ssl_error,
                                    client, route, valid_jwt, valid_json,
                                    ssl_error_expected_relay_response):

    mock_get.return_value = \
        mock_api_response(payload=EXPECTED_RESPONSE_OF_JWKS_ENDPOINT)
    mock_request.side_effect = [SSLError(mock_exception_for_ssl_error)]

    response = client.post(route, headers=get_headers(valid_jwt()),
                           json=valid_json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == ssl_error_expected_relay_response
