import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class GoogleService:
    def get_coordinates(self, params):
        response = self.connection(params)
        json = response.json()
        if response.status_code == 200 and 'results' in json.keys():
            coordinates = {}
            coordinates.update({'latitude': json['results'][0]['geometry']['location']['lat']})
            coordinates.update({'longitude': json['results'][0]['geometry']['location']['lng']})
            return coordinates
        else:
            content = {'Invalid Address': 'Please enter a street address, city, and state.'}
            return content

    def connection(self, params):
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        return requests.get(url, params)
