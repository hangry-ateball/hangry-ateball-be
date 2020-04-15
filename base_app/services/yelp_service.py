import json
import os
import random
import requests
from base_app.models.restaurant import Restaurant
from base_app.models.restaurant_schema import RestaurantSchema
from base_app.services.google_service import GoogleService
from dotenv import load_dotenv
load_dotenv()

class YelpService:

    def get_recommendation(self, params):
        restaurant_id = self.get_restaurant(params)
        if restaurant_id:
            url = 'https://api.yelp.com/v3/businesses/{}'.format(restaurant_id)
            response = self.connection(url)
            json_data = json.dumps(response.json())
            if isinstance(response.json()['coordinates']['latitude'], float):
                google_service = GoogleService()
                website = google_service.get_website(json_data)
            elif 'url' in response.json().keys(): # Will return the Restaurant's Yelp Business Page if no Coordinates available
                website = response.json()['url']
            recommendation = Restaurant.from_json(json_data, website)
            schema = RestaurantSchema()
            result = schema.dump(recommendation)
            return result
        elif 'radius' in params.keys() and params['radius'] == 16000:
            params.pop('radius', None)
            self.get_recommendation(params)
        else:
            return {'error': "It appears there aren't any restaurants open near you right now."}

    def get_restaurant(self, params):
        url = 'https://api.yelp.com/v3/businesses/search'
        response = self.connection(url, params)
        all = response.json()
        ids = []
        if response.status_code == 200 and 'businesses' in all.keys():
            for x in all['businesses']:
                if x.get('price') != None:
                    ids.append(x['id'])
                else:
                    continue
        if len(ids) != 0:
            restaurant_id = random.choice(ids)
            return restaurant_id
        else:
            return False

    def connection(self, url, params = ''):
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + YELP_API_KEY}
        return requests.get(url, params=params, headers=headers)
