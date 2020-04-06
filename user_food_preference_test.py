import requests
import json
import pdb
from base import app
from flask import Flask
from instance import config

def test_can_connect_to_api_endpoint():
    client = app.test_client()
    response = client.get('/api/v1/recommendations')

    assert response.data == b'Hello, World!'

def test_user_selects_food_preference_returns_successful_response():
    headers = { 'authorization': config.YELP_API_KEY }
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    params = { 'latitude': lat, 'longitude': long, 'term': cuisine }
    url = "https://api.yelp.com/v3/businesses/search?latitude=% s&longitude=% s&term=% s"%(lat, long, cuisine)

    response = requests.get(url, headers=headers)

    assert response.status_code == 200

def test_user_selects_food_preference_returns_restaurant_data():
    headers = { 'authorization': config.YELP_API_KEY }
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    params = { 'latitude': lat, 'longitude': long, 'term': cuisine }
    url = "https://api.yelp.com/v3/businesses/search"

    response = requests.get(url, params=params, headers=headers)
    response_body = response.json()
    first_business = response_body['businesses'][0]

    assert first_business['name'] == 'Mint Indian Restaurant & Lounge'
    assert first_business['location']['display_address'] == ['1531 Stout St', 'Ste 130', 'Denver, CO 80202']
    assert first_business['display_phone'] == '(720) 931-1111'
    assert first_business['price'] ==  '$$'
    assert first_business['rating'] == 4.0

    # response_body include images
    # response_body include website url
    # response_body include menu
