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

    def get_place_id(self, params):
        url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
        params.update({'inputtype': 'textquery')
        response = self.connection(url, params)
        if response.status_code == 200 and 'candidates' in response.json.keys():
            return response.json['candidates'][0]['place_id']
        else:
            return {'Invalid Request': 'Params required are locationbias: point:<lat>,<long> -and- input: <restaurant_name>'}

    def get_website(self, json_data):
        yelp_data = json.loads(json_data)
        lat = yelp_data['coordinates']['latitude']
        long = yelp_data['coordinates']['longitude']
        place_id_params = {'locationbias': f'point:{lat},{long}', 'input': yelp_data['name']}
        place_id = self.get_place_id(place_id_params)

        params = {'place_id': place_id}
        url = 'https://maps.googleapis.com/maps/api/place/details/json'
        response = self.connection(url, params)
        if response.status_code == 200: and 'result' in response.json.keys():
            return response.json['result']['website']
