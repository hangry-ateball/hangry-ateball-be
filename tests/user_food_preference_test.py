import os
import requests
from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

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

def test_user_selects_food_preference_returns_restaurant_data():
    YELP_API_KEY = os.getenv('YELP_API_KEY')
    headers = {'authorization': 'Bearer ' + YELP_API_KEY}
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    params = {'latitude': lat, 'longitude': long, 'term': cuisine}
    url = "https://api.yelp.com/v3/businesses/search"

    response = requests.get(url, params=params, headers=headers)
    response_body = response.json()
    first_business = response_body['businesses'][0]

    assert first_business['name'] == 'Mint Indian Restaurant & Lounge'
    assert first_business['categories'][0]['title'] == 'Indian'
    assert first_business['location']['display_address'] == ['1531 Stout St', 'Ste 130', 'Denver, CO 80202']
    assert first_business['phone'] == '+17209311111'
    assert first_business['display_phone'] == '(720) 931-1111'
    assert first_business['rating'] == 4.0
    assert first_business['price'] == '$$'

    # response_body include images
    # response_body include website url
    # response_body include menu
