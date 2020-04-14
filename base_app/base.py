from flask_cors import CORS
from flask import Flask, request, render_template
from base_app.services.google_service import GoogleService
from base_app.services.twilio_service import TwilioService
from base_app.services.yelp_service import YelpService
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
cors = CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Hangry Ateball API'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix = SWAGGER_URL)

@app.route('/', methods=['GET'])
@app.route('/api/v1', methods=['GET'])
def home():
    return render_template('index.html', title = 'Hangry Ateball')

@app.route('/api/v1/recommendations', methods=['GET'])
def index():
    service = YelpService()
    params = format_params(request.args)
    return service.get_recommendation(params)

@app.route('/api/v1/random', methods=['GET'])
def get_random():
    service = YelpService()
    params = format_params(request.args)
    return service.get_recommendation(params)

@app.route('/api/v1/notify', methods=['GET'])
def notify():
    from_ = '+' + request.args['from']
    to = '+' + request.args['to']
    body = request.args['body']
    client = TwilioService.get_client()
    message = client.messages.create(
        body='Hangry Ateball invites you to join your friend at {}'.format(body),
        from_=from_,
        to=to
    )
    return message.status

## Helper Methods ##

def has_address(request_args):
    params = {'open_now': True, 'term': 'food'}
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
            params.update({'price': '1,2'})
        elif request.args['price'] == 3:
            params.update({'price': '1,2,3'})
        else:
            params.update({'price': request.args['price']})

    if 'categories' in request.args.keys():
        cuisine = request.args['categories']
        params.update({'term': f'{cuisine}'})

    if 'travel' in request.args.keys() and request.args['travel'] == 'walk':
        params.update({'radius': 1600})
    else:
        params.update({'radius': 16000})

    return params

if __name__ == '__main__':
    app.run()
