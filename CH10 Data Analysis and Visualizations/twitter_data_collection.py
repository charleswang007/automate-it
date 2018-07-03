from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#consumer key, consumer secret, access token, access secret.
ckey='PMjg2sgb9WQCPN2DUjEH4lLpL'
csecret='KhIRi19EgJE9960PaS12GjXYEltR3OBG3O64hHFOpuXrS9L6bk'
atoken='510696917-CV5RjVIElEKj4UkAqNt6Y7nM5m2LcPe7loObuItG'
asecret='93idoc5xrWuyezbc0ENBGj56uo0BMps54zrcnyvB00T5w'

tweets_data_path = 'twitter_data_new.txt'
f = open(tweets_data_path, "w")

#Inherit stream listener to get the twitter data
class listener(StreamListener):

    def on_data(self, data):
	print data
        #Store twitter data in a text file	
	f.write(data)

        #You can also access data this way
        #all_data = json.loads(data)
        #tweet = all_data["text"]
        #lang = all_data["lang"]
        #username = all_data["user"]["screen_name"]
        #print "username:%s, tweet:%s, language:%s" %(username, tweet, lang)

        return True

    def on_error(self, status):
        print "Error:", status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#Filter twitter stream based on "iPhone 7" and "Note 5"
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["lebron","durant"])
f.close()
