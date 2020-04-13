from base_app.yelp_service import YelpService
from dotenv import load_dotenv
load_dotenv()

def test_can_initialize():
    service = YelpService()
    assert isinstance(service, YelpService)

def test_can_connect():
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'latitude': '39.7392358', 'longitude': '-104.990251'}

    service = YelpService()
    response = service.connection(url, params)

    assert response.status_code == 200
    assert 'businesses' in response.json()

def test_can_get_recommendation():
    params = {'latitude': '39.7392358', 'longitude': '-104.990251'}

    service = YelpService()
    response = service.get_recommendation(params)

    assert 'id' in response['data']
    assert 'cuisine' in response['data']['attributes']
    assert 'name' in response['data']['attributes']
    assert 'location' in response['data']['attributes']
    assert 'phone' in response['data']['attributes']
    assert 'display_phone' in response['data']['attributes']
    assert 'rating' in response['data']['attributes']
    assert 'price' in response['data']['attributes']
    assert 'photos' in response['data']['attributes']
    assert response['data']['attributes']['is_closed'] == False




