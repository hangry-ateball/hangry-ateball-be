import os
import unittest
import vcr
from base_app.yelp import Yelp
from dotenv import load_dotenv
load_dotenv()

class YelpTest(unittest.TestCase):
    def setUp(self):
        self.test_api_key = os.getenv('YELP_API_KEY')

    @vcr.use_cassette(
        'fixtures/cassettes/test_get_recommendation.yml',
        filter_headers=['authorization']
    )

    def test_can_connect(self):
        url = 'https://api.yelp.com/v3/businesses/search'
        params = {'latitude': '39.7392358', 'longitude': '-104.990251'}

        service = Yelp(self.test_api_key)
        response = service.connection(url, params)

        assert response.status_code == 200
        assert 'businesses' in response.json()

    def test_can_get_recommendation(self):
        params = {'latitude': '39.7392358', 'longitude': '-104.990251'}

        service = Yelp(self.test_api_key)
        response = service.get_recommendation(params)

        assert 'id' in response['data']
        assert 'cuisine' in response['data']['attributes']
        assert 'name' in response['data']['attributes']
        assert 'location' in response['data']['attributes']
        assert 'phone' in response['data']['attributes']
        assert 'display_phone' in response['data']['attributes']
        assert 'rating' in response['data']['attributes']
        assert 'price' in response['data']['attributes']
        assert 'photos' in response['data']['attributes']
        assert response['data']['attributes']['is_closed'] == False
