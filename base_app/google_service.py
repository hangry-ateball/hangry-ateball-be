import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

class GoogleService:
    def connection(self, url, params):
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        response = requests.get(url, params)
        return response

