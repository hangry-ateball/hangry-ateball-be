import os
import unittest
import vcr
from base_app.google import Google
from dotenv import load_dotenv
load_dotenv()

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.test_api_key = os.getenv('GOOGLE_API_KEY')

    @vcr.use_cassette(
        'fixtures/cassettes/test_returns_coordinates.yml',
        filter_query_parameters=['key']
    )

    def test_can_connect(self):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        address = '1331 17th St LL100, Denver, CO'
        params = {'key': self.test_api_key, 'address': f'{address}'}

        service = Google(self.test_api_key)
        response = service.connection(url, params)

        assert response.status_code == 200

    def test_google_api_returns_coordinates_with_street_address(self):
        address = '1331 17th St LL100, Denver, CO'
        params = {'key': self.test_api_key, 'address': f'{address}'}

        service = Google(self.test_api_key)
        response = service.get_coordinates(params)

        assert response == {'latitude': 39.7508006, 'longitude': -104.9965947}

    def test_google_api_returns_coordinates_with_city_and_state(self):
        address = 'Denver, CO'
        params = {'key': self.test_api_key, 'address': f'{address}'}
        service = Google(self.test_api_key)
        response = service.get_coordinates(params)
        assert response == {'latitude': 39.7392358, 'longitude': -104.990251}

    def test_google_api_returns_coordinates_with_only_city(self):
        address = 'Denver'
        params = {'key': self.test_api_key, 'address': f'{address}'}
        service = Google(self.test_api_key)
        response = service.get_coordinates(params)
        assert response == {'latitude': 39.7392358, 'longitude': -104.990251}

    def test_google_api_returns_coordinates_with_only_state(self):
        address = 'Colorado'
        params = {'key': self.test_api_key, 'address': f'{address}'}
        service = Google(self.test_api_key)
        response = service.get_coordinates(params)
        assert response == {'latitude': 39.5500507, 'longitude': -105.7820674}

    def test_google_api_returns_error_if_invalid_address_submitted(self):
        address = '123 Test Street'
        params = {'key': self.test_api_key, 'input': f'{address}'}
        service = Google(self.test_api_key)
        response = service.get_coordinates(params)
        assert response == {'Invalid Address': 'Please enter a street address, city, and state.'}
