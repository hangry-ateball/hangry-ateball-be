import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class TwilioService:
    def get_client():
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        return Client(account_sid, auth_token)
