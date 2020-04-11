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
        YELP_API_KEY = os.getenv('YELP_API_KEY')
        headers = {'authorization': 'Bearer ' + YELP_API_KEY}
        url = 'https://api.yelp.com/v3/businesses/search'

        response = requests.get(url, params=params, headers=headers)

        json_data = json.dumps(response.json())
        restaurants = Restaurant.from_json(json_data)
        restaurant = random.choice(restaurants)
        schema = RestaurantSchema()
        result = schema.dump(restaurant)
        return result
