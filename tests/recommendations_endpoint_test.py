from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

def test_user_selects_multiple_preferences_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    price = '2'
    url = '/api/v1/recommendations?latitude={}&longitude={}&categories={}&price={}'.format(lat, long, cuisine, price)

    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200

    response_body = response.json

    assert 'id' in response_body['data']
    assert 'cuisine' in response_body['data']['attributes']
    assert 'name' in response_body['data']['attributes']
    assert 'location' in response_body['data']['attributes']
    assert 'phone' in response_body['data']['attributes']
    assert 'display_phone' in response_body['data']['attributes']
    assert 'rating' in response_body['data']['attributes']
    assert 'price' in response_body['data']['attributes']

def test_user_selects_food_preference_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    url = '/api/v1/recommendations?latitude={}&longitude={}&categories={}'.format(lat, long, cuisine)

    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200

    response_body = response.json

    assert 'id' in response_body['data']
    assert 'cuisine' in response_body['data']['attributes']
    assert 'name' in response_body['data']['attributes']
    assert 'location' in response_body['data']['attributes']
    assert 'phone' in response_body['data']['attributes']
    assert 'display_phone' in response_body['data']['attributes']
    assert 'rating' in response_body['data']['attributes']
    assert 'price' in response_body['data']['attributes']

def test_user_selects_price_preference_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '2'

    url = '/api/v1/recommendations?latitude={}&longitude={}&price={}'.format(lat, long, price)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    assert 'id' in response_body ['data']
    assert 'cuisine' in response_body['data']['attributes']
    assert 'name' in response_body['data']['attributes']
    assert 'location' in response_body['data']['attributes']
    assert 'phone' in response_body['data']['attributes']
    assert 'display_phone' in response_body['data']['attributes']
    assert 'rating' in response_body['data']['attributes']
    assert 'price' in response_body['data']['attributes']


