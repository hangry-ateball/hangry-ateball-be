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
    text = response.data
    assert text == b'<h1>Welcome to the Hangry-8Ball API!</h1><p>Enter API documentation and endpoints here.</p>'