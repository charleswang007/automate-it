#from flask import Flask
import requests
import twilio.twiml
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse

app = Flask(__name__)

#flask route to work on callback url for incoming SMS
@app.route("/insms", methods=['GET', 'POST'])
def respond_sms():
    #resp = twilio.twiml.Response()
    resp = MessagingResponse()
    #resp.message("Thanks for your query --- James Bond the 007")
    #return str(resp)
    message = Message()
    message.body('Republic of China')
    message.media('http://s580789446.onlinehome.us/calligraphy/images/2009-4.JPG')
    resp.append(message)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
