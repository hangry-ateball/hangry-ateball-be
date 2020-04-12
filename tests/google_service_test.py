import os
import requests
from base_app.base import app
from dotenv import load_dotenv
load_dotenv()

def test_google_api_returns_successful_response():
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    url = https://maps.googleapis.com/
    params = {'key': GOOGLE_API_KEY }
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=#{}'.format()


def test_google_api_returns_coordinates():