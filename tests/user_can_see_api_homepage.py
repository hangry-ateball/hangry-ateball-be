import os
import requests
from base_app.base import app

def test_user_selects_food_preference_returns_successful_response():
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    url = '/api/v1/recommendations?latitude={}&longitude={}&categories={}'.format(lat, long, cuisine)

    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200