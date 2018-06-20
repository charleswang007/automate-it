import config
from flask import Flask
#from twilio.rest import TwilioRestClient
from twilio.rest import Client

#Create a flask app and twilio client object
app = Flask(__name__)
#client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
#                          config.TWILIO_AUTH_TOKEN)
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

#Send a message from Twilio
message = client.messages.create(
    to=config.MYNUMBER,
    from_=config.CALLERID,
    media_url='https://pic.funnygifsbox.com/uploads/2014/09/5c92fb79ad481f9a0ce640845a074ea0.gif',
    body="Hey Allen! Can you receive this message? --- Kobe")

