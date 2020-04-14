import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class GoogleService:
    def connection(self, url, params):
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        params.update({'key': GOOGLE_API_KEY})
        return requests.get(url, params)

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


