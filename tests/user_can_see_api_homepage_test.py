import os
import requests
from base_app.base import app

def test_homepage_returns_successful_response():
    url = '/'
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == 200

def test_homepage_returns_documentation_info():
    url = '/'
    client = app.test_client()
    response = client.get(url)
    text = response.data.decode('utf8')
    assert text == '<h1>Welcome to the Hangry AteBall API!</h1>\n<p>You can find the API documentation at\n    <a href="https://hangry-ateball-api.herokuapp.com/api/docs">https://hangry-ateball-api.herokuapp.com/api/docs</a>.\n</p>'