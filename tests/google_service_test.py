import os
import requests
from base_app.base import app
from base_app.google_service import GoogleService
from dotenv import load_dotenv
load_dotenv()

def test_can_initialize():
    service = GoogleService()
    assert isinstance(service, GoogleService)

def test_google_api_returns_successful_response():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = '1331 17th St LL100, Denver, CO'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    service = GoogleService()
    response = service.connection(url, params)
    status = response.status_code
    assert response.status_code == 200

def test_google_api_returns_coordinates_with_street_address():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = '1331 17th St LL100, Denver, CO'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    service = GoogleService()
    response = service.connection(url, params)
    response = response.json()
    assert response['results'][0]['geometry']['location']['lat'] == 39.7508006
    assert response['results'][0]['geometry']['location']['lng'] == -104.9965947

def test_google_api_returns_coordinates_with_city_and_state():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = 'Denver, CO'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    service = GoogleService()
    response = service.connection(url, params)
    response = response.json()
    assert response['results'][0]['geometry']['location']['lat'] == 39.7392358
    assert response['results'][0]['geometry']['location']['lng'] == -104.990251