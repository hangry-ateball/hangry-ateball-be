from flask import Flask, request
from base_app.yelp_service import YelpService
from base_app.google_service import GoogleService
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome to the Hangry-8Ball API!</h1><p>Enter API documentation and endpoints here.</p>"

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    service = YelpService()
    params = format_params(request.args)
    return service.get_recommendation(params)

@app.route('/api/v1/random', methods=['GET'])
def get_random():
    service = YelpService()
    params = format_params(request.args)
    return service.get_recommendation(params )

## Helper Methods ##

def has_address(request_args):
    params = { 'open_now': True, 'term': 'food'}
    google = GoogleService()
    location = {}
    new_address = request_args['address'].replace(",", "+")
    location.update({'address': f'{new_address}'})
    coordinates  = google.get_coordinates(location)
    params.update(coordinates)
    return params

def format_params(request_args):
    if 'address' in request.args.keys():
        params = has_address(request_args)
    else:
        params = {'latitude': request_args['latitude'], 'longitude': request_args['longitude'], 'open_now': True, 'term': 'food'}

    if 'price' in request.args.keys():
        if request.args['price'] == 2:
            params.update({"price": "1,2"})
        elif request.args['price'] == 3:
            params.update({"price": "1,2,3"})
        else:
            params.update({"price": request.args['price']})

    if 'categories' in request.args.keys():
        cuisine = request.args['categories']
        params.update({"term": f'{cuisine}'})

    return params


if __name__ == '__main__':
    app.run()


