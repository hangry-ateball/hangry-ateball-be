import json
import os
import random
import requests
from base_app.restaurant import Restaurant
from base_app.restaurant_schema import RestaurantSchema
from base_app.photo import Photo
from base_app.photo_schema import PhotoSchema
from dotenv import load_dotenv
load_dotenv()

class YelpService:

    def get_recommendation(self, params):
        restaurant_id = self.get_restaurant(params)
        url = 'https://api.yelp.com/v3/businesses/{}'.format(restaurant_id)
        response = self.connection(url)
        json_data = json.dumps(response.json())
        recommendation = Restaurant.from_json(json_data)
        schema = RestaurantSchema()
        result = schema.dump(recommendation)
        return result

    def get_restaurant(self, params):
        url = 'https://api.yelp.com/v3/businesses/search'
        response = self.connection(url, params)
        all = response.json()
        for x in all['businesses']:
            if x.get('price') != None:
                ids = []
                ids.append(x['id'])
            else:
                continue
        return random.choice(ids)

    def connection(self, url, params = ''):
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + YELP_API_KEY}
        return requests.get(url, params=params, headers=headers)
