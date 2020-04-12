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
    price = len(response_body['data']['attributes']['price'])

    assert 'id' in response_body['data']
    assert 'cuisine' in response_body['data']['attributes']
    assert 'name' in response_body['data']['attributes']
    assert 'location' in response_body['data']['attributes']
    assert 'phone' in response_body['data']['attributes']
    assert 'display_phone' in response_body['data']['attributes']
    assert 'rating' in response_body['data']['attributes']
    assert 'price' in response_body['data']['attributes']
    assert price <= 2
    assert response_body['data']['attributes']['is_closed'] == False

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
    assert response_body['data']['attributes']['is_closed'] == False

def test_user_selects_price_preference_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '3'

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
    assert response_body['data']['attributes']['is_closed'] == False

def test_user_selects_price_preference_1_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '1'

    url = '/api/v1/recommendations?latitude={}&longitude={}&price={}'.format(lat, long, price)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    price = len(response_body['data']['attributes']['price'])
    assert 'price' in response_body['data']['attributes']
    assert price == 1
    assert response_body['data']['attributes']['is_closed'] == False

def test_user_selects_price_preference_2_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '2'

    url = '/api/v1/recommendations?latitude={}&longitude={}&price={}'.format(lat, long, price)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    price = len(response_body['data']['attributes']['price'])
    assert 'price' in response_body['data']['attributes']
    assert price <= 2
    assert response_body['data']['attributes']['is_closed'] == False

def test_user_selects_price_preference_3_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '3'

    url = '/api/v1/recommendations?latitude={}&longitude={}&price={}'.format(lat, long, price)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    price = len(response_body['data']['attributes']['price'])
    assert 'price' in response_body['data']['attributes']
    assert price <= 3
    assert response_body['data']['attributes']['is_closed'] == False

def test_user_selects_price_preference_4_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    price = '4'

    url = '/api/v1/recommendations?latitude={}&longitude={}&price={}'.format(lat, long, price)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    price = len(response_body['data']['attributes']['price'])
    assert 'price' in response_body['data']['attributes']
    assert price == 4
    assert response_body['data']['attributes']['is_closed'] == False





