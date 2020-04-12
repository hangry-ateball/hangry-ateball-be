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
