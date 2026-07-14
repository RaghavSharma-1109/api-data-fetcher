import requests
from api.fetcher import get_crypto_prices


def test_get_crypto_price_success(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'bitcoin':{'usd':50000}}

    mocker.patch("api.fetcher.requests.get", return_value=mock_response)

    result = get_crypto_prices(['bitcoin'],['inr'])

    assert result['success'] is True
    assert result['data'] == {'bitcoin':{'usd':50000}}
    assert result['error'] is None

def test_get_crypto_price_non200(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mocker.patch("api.fetcher.requests.get", return_value=mock_response)

    result = get_crypto_prices(['bitcoin'],['inr'])

    assert result['success'] is False
    assert result['data'] is None
    assert result['error'] == 'API returned error response'

def test_get_crypto_price_tiemout(mocker):

    mocker.patch("api.fetcher.requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))

    result = get_crypto_prices(['bitcoin'],['inr'])

    assert result['success'] is False
    assert result['data'] is None
    assert result['error'] == 'Request Timed out'

def test_get_crypto_price_connection(mocker):

    mocker.patch("api.fetcher.requests.get", side_effect=requests.exceptions.ConnectionError("Connection error"))

    result = get_crypto_prices(['bitcoin'],['inr'])

    assert result['success'] is False
    assert result['data'] is None
    assert result['error'] == 'Connection error'

def test_get_crypto_price_Http(mocker):

    mocker.patch("api.fetcher.requests.get", side_effect=requests.exceptions.HTTPError("Unexpected API response"))

    result = get_crypto_prices(['bitcoin'],['inr'])

    assert result['success'] is False
    assert result['data'] is None
    assert result['error'] == 'Unexpected API response'