import json
import os
import random
import requests
from flask import Flask, request
from base_app.restaurant import Restaurant
from base_app.restaurant_schema import RestaurantSchema
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Hangry-8Ball API!</h1><p>Enter API documentation and endpoints here.</p>"

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    YELP_API_KEY = os.getenv('YELP_API_KEY')
    headers = {'authorization': 'Bearer ' + YELP_API_KEY}
    lat = request.args['latitude']
    long = request.args['longitude']
    cuisine = request.args['categories']
    params = {'latitude': f'{lat}', 'longitude': f'{long}', 'term': f'{cuisine}'}
    url = 'https://api.yelp.com/v3/businesses/search'

    response = requests.get(url, params=params, headers=headers)
    json_data = json.dumps(response.json())
    restaurants = Restaurant.from_json(json_data)
    restaurant = random.choice(restaurants)
    schema = RestaurantSchema()
    result = schema.dump(restaurant)

    return result

if __name__ == '__main__':
    app.run(debug=True)
