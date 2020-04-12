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
    service = GoogleService()
    response = service.connection(params)
    status = response.status_code
    assert response.status_code == 200

def test_google_api_returns_coordinates_with_street_address():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = '1331 17th St LL100, Denver, CO'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    service = GoogleService()
    response = service.get_coordinates(params)
    assert response == { 'latitude': 39.7508006, 'longitude': -104.9965947 }

def test_google_api_returns_coordinates_with_city_and_state():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = 'Denver, CO'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    service = GoogleService()
    response = service.get_coordinates(params)
    assert response == {'latitude': 39.7392358, 'longitude': -104.990251}

def test_google_api_returns_coordinates_with_only_city():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = 'Denver'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    service = GoogleService()
    response = service.get_coordinates(params)
    assert response == {'latitude': 39.7392358, 'longitude': -104.990251}

def test_google_api_returns_coordinates_with_only_state():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = 'Colorado'
    params = {'key': GOOGLE_API_KEY, 'address': f'{address}' }
    service = GoogleService()
    response = service.get_coordinates(params)
    assert response == { 'latitude': 39.5500507, 'longitude': -105.7820674 }

def test_google_api_returns_error_if_invalid_address_submitted():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    address = '123 Test Street'
    params = {'key': GOOGLE_API_KEY, 'input': f'{address}'}
    service = GoogleService()
    response = service.get_coordinates(params)
    assert response == {'Invalid Address': 'Please enter a street address, city, and state.'}
