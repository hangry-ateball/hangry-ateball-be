import os
import requests
from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

def test_user_selects_random_restaurant_option_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    url = '/api/v1/random?latitude={}&longitude={}'.format(lat, long)

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
    assert 'photos' in response_body['data']['attributes']

