import json
import os
import random
import requests
from flask import Flask, request
from base_app.restaurant import Restaurant
from base_app.restaurant_schema import RestaurantSchema
from base_app.photo import Photo
from base_app.photo_schema import PhotoSchema
from base_app.yelp_service import YelpService
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Hangry-8Ball API!</h1><p>Enter API documentation and endpoints here.</p>"

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    service = YelpService()
    lat = request.args['latitude']
    long = request.args['longitude']
    params = {'latitude': f'{lat}', 'longitude': f'{long}'}

    if 'price' in request.args.keys():
         params.update({"price": request.args['price']})

    if 'categories' in request.args.keys():
        cuisine = request.args['categories']
        params.update({"term": f'{cuisine}'})

    return service.get_recommendation(params)


@app.route('/api/v1/photos', methods=['GET'])
def get_photos():
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

    restaurant_id = result['data']['id']
    restaurant_url = f'https://api.yelp.com/v3/businesses/{restaurant_id}'

    response = requests.get(restaurant_url, headers=headers)
    json_data = json.dumps(response.json())
    photos = Photo.from_json(json_data)
    schema = PhotoSchema()
    result = schema.dump(photos)

    return result

if __name__ == '__main__':
    app.run(debug=True)
