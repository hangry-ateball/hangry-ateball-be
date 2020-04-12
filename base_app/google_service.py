import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class GoogleService:
    def connection(self, params):
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        response = requests.get(url, params)
        json = response.json()
        if response.status_code == 200 and 'results' in json.keys():
            return response
        else:
            content = {'Invalid Address': 'Please enter a street address, city, and state.'}
            return content

