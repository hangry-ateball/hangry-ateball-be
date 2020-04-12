from flask import Flask, request
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
    params = format_params(request.args)
    return service.get_recommendation(params)

## Helper Methods ##

def format_params(request_args):
    params = {'latitude': request_args['latitude'], 'longitude': request_args['longitude'], 'open_now': True}

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


@app.route('/api/v1/random', methods=['GET'])
def get_random():
    YELP_API_KEY = os.getenv('YELP_API_KEY')
    headers = {'authorization': 'Bearer ' + YELP_API_KEY}
    lat = request.args['latitude']
    long = request.args['longitude']
    business_type = 'food'
    open = True
    params = {'latitude': f'{lat}', 'longitude': f'{long}', 'term': f'{business_type}', 'open_now': f'{open}'}
    url = 'https://api.yelp.com/v3/businesses/search'

    response = requests.get(url, params=params, headers=headers)
    json_data = json.dumps(response.json())
    restaurants = Restaurant.from_json(json_data)
    restaurant = random.choice(restaurants)
    schema = RestaurantSchema()
    result = schema.dump(restaurant)

    return result

if __name__ == '__main__':
    app.run()


