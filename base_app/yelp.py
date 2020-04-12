import json
import os
import random
import requests
from base_app.restaurant import Restaurant
from base_app.restaurant_schema import RestaurantSchema
from dotenv import load_dotenv
load_dotenv()

class Yelp(object):
    def __init__(self, api_key):
        self.api_key = api_key

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
        self.api_key = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + self.api_key}
        return requests.get(url, params=params, headers=headers)
