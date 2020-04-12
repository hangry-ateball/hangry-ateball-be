import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class Google(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_coordinates(self, params):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        response = self.connection(url, params)
        json = response.json()
        if response.status_code == 200 and 'results' in json.keys():
            coordinates = {}
            coordinates.update({'latitude': json['results'][0]['geometry']['location']['lat']})
            coordinates.update({'longitude': json['results'][0]['geometry']['location']['lng']})
            return coordinates
        else:
            content = {'Invalid Address': 'Please enter a street address, city, and state.'}
            return content

    def connection(self, url, params = ''):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        return requests.get(url, params=params)
