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
        url = 'https://api.yelp.com/v3/businesses/search'
        response = self.connection(url, params)
        json_data = json.dumps(response.json())
        restaurants = Restaurant.from_json(json_data)
        restaurant = random.choice(restaurants)
        schema = RestaurantSchema()
        result = schema.dump(restaurant)
        return result

    def get_photos(self, restaurant_result):
        restaurant_id = restaurant_result['data']['id']
        restaurant_url = f'https://api.yelp.com/v3/businesses/{restaurant_id}'

        response = self.connection(restaurant_url)
        json_data = json.dumps(response.json())
        photos = Photo.from_json(json_data)
        schema = PhotoSchema()
        result = schema.dump(photos)
        return result

    def connection(self, url, params = ''):
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + YELP_API_KEY}
        return requests.get(url, params=params, headers=headers)
