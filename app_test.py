import requests
def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
     response = requests.get("http://api.zippopotam.us/us/90210")
     response_body = response.json()
     assert response_body["places"][0]["place name"] == "Beverly Hills"
