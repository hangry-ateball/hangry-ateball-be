import json
import os
import random
import requests
from base_app.restaurant import Restaurant
from base_app.restaurant_schema import RestaurantSchema
from dotenv import load_dotenv
load_dotenv()

class YelpService:

    def get_recommendation(self, params):
        info = self.get_restaurant(params)
        restaurant_id = info[0]
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
        ids = {}
        for x in all['businesses']:
            if x.get('price') != None:
                ids.update({x['id']: x['distance']})
            else:
                continue
        restaurant = random.choice(list(ids.items()))
        return restaurant

    def connection(self, url, params = ''):
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + YELP_API_KEY}
        return requests.get(url, params=params, headers=headers)
