#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
from flask import Flask, Response, request
from twilio import twiml
#from twilio.rest import TwilioRestClient
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)
#client = TwilioRestClient(config.TWILIO_ACCOUNT_SID,
#                          config.TWILIO_AUTH_TOKEN)
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)

#Clask app to receive incoming calls
@app.route('/incall', methods=['POST'])
def inbound_call():
    #response = twiml.Response()
    response = VoiceResponse()
    #Once the call is received, respond with the below message to the caller
    response.say(u'曾經年少愛追夢', voice="alice", language='zh-TW')
    response.pause(length=1)
    response.say(u'一心只想往前飛', voice="alice", language='zh-TW')
    response.pause(length=1)
    response.say(u'行遍千山和萬水', voice="alice", language='zh-TW')
    response.pause(length=1)
    response.say(u'一路走來不能回', voice="alice", language='zh-TW')
    #response.say("Thanks for being a loyal member of South Bay Taiwanese People Meetup. President Charles appreicates your particiaption. Have a nice day. Bond. James Bond.", voice="man")
    return Response(str(response), 200, mimetype="application/xml")

if __name__ == '__main__':
    app.run(debug=True)

