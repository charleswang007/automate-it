#from flask import Flask
import requests
import twilio.twiml
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
from textblob import TextBlob

app = Flask(__name__)

#flask route to work on callback url for incoming SMS
@app.route("/insms", methods=['GET', 'POST'])
def respond_sms():
    #resp = twilio.twiml.Response()
    resp = MessagingResponse()
    body = request.form['Body']
    blob = TextBlob(body)
    message = Message()
    #resp.message("Thanks for your query --- James Bond the 007")
    #return str(resp)
    try:
        number = int(str(blob))
        message.body("Thanks - You entered number " + str(blob) + ". Your guess is " + str(abs(32 - number)) + " away from the correct answer: 32. We will let you know if your guess is one of the 10 closest very soon. - CHARLES")
        #message.body('Republic of China')
        #message.media('http://s580789446.onlinehome.us/calligraphy/images/2009-4.JPG')
        resp.append(message)
        return str(resp)
    except:
        return "Unexpected Error! Please enter only integer from 0 to 60."

if __name__ == "__main__":
    app.run(debug=True)
