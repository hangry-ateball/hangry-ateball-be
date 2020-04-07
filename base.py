from flask import Flask, request
import json
import requests
import random
from instance import config
from restaurant import Restaurant
from restaurant_schema import RestaurantSchema
from marshmallow_jsonapi import Schema, fields

app = Flask(__name__)

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    headers = { 'authorization': config.YELP_API_KEY }
    lat = request.args['latitude']
    long = request.args['longitude']
    cuisine = request.args['categories']
    params = {'latitude': f"{lat}", 'longitude': f"{long}", 'term': f"{cuisine}"}
    url = "https://api.yelp.com/v3/businesses/search"
    response = requests.get(url, params=params, headers=headers)
    data = json.dumps(response.json())
    restaurants = Restaurant.from_json(data)
    restaurant = random.choice(restaurants)
    schema = RestaurantSchema()
    result = schema.dump(restaurant)
    return result

if __name__ == '__main__':
    app.run(debug=True)
