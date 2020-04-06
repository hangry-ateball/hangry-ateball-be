from flask import Flask
import requests
from instance import config

app = Flask(__name__)

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    headers = { 'authorization': config.YELP_API_KEY }
    lat = '39.7392358'
    long = '-104.990251'
    cuisine = 'indian'
    params = { 'latitude': lat, 'longitude': long, 'term': cuisine }
    url = "https://api.yelp.com/v3/businesses/search"

    response = requests.get(url, params=params, headers=headers)

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
