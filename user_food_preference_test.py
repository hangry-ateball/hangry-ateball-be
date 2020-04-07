import requests
import json
import pdb
from flask import Flask
from instance import config
from base import app

def test_user_selects_food_preference_returns_successful_response():
    client = app.test_client()

    headers = { 'authorization': config.YELP_API_KEY }
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    params = { 'latitude': lat, 'longitude': long, 'categories': cuisine }
    response = client.get("/api/v1/recommendations?latitude=% s&longitude=% s&categories=% s"%(lat, long, cuisine))
    response_body = json.loads(response.data.decode('utf8'))

    assert response.status_code == 200
    assert 'id' in response_body['data']
    assert 'cuisine' in response_body['data']['attributes']
    assert 'display_phone' in response_body['data']['attributes']
    assert 'location' in response_body['data']['attributes']
    assert 'name' in response_body['data']['attributes']
    assert 'phone' in response_body['data']['attributes']
    assert 'price' in response_body['data']['attributes']
    assert 'rating' in response_body['data']['attributes']

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
