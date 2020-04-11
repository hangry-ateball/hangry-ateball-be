from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

def test_user_selects_multiple_preferences_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    price = '2'
    travel = 'walk'
    url = '/api/v1/recommendations?latitude={}&longitude={}&categories={}&price={}&travel={}'.format(lat, long, cuisine, price, travel)

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

def test_user_selects_travel_preference_walk_returns_correct_distance():
    lat = '39.7392358'
    long = '-104.990251'
    travel = 'walk'

    url = '/api/v1/recommendations?latitude={}&longitude={}&travel={}'.format(lat, long, travel)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    assert 'distance' in response_body['data']['attributes']
    assert response_body['data']['attributes']['distance'] <= 1700

def test_user_selects_travel_preference_drive_returns_correct_distance():
    lat = '39.7392358'
    long = '-104.990251'
    travel = 'drive'

    url = '/api/v1/recommendations?latitude={}&longitude={}&travel={}'.format(lat, long, travel)
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

    response_body = response.json
    assert 'distance' in response_body['data']['attributes']
    assert response_body['data']['attributes']['distance'] <= 17000
