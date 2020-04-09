import os
import requests
from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

def test_retrieve_restaurant_photos_when_user_submits_preferences():
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'spanish'
    url = '/api/v1/photos?latitude={}&longitude={}&categories={}'.format(lat, long, cuisine)

    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200

    response_body = response.json

    assert 'id' in response_body['data']
    assert 'type' in response_body['data']
    assert 'photos' in response_body['data']['attributes']
