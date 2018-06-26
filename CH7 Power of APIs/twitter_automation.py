from twython import Twython

APP_KEY = 'PMjg2sgb9WQCPN2DUjEH4lLpL'
APP_SECRET = 'KhIRi19EgJE9960PaS12GjXYEltR3OBG3O64hHFOpuXrS9L6bk'
OAUTH_TOKEN ='510696917-CV5RjVIElEKj4UkAqNt6Y7nM5m2LcPe7loObuItG'
OAUTH_TOKEN_SECRET = '93idoc5xrWuyezbc0ENBGj56uo0BMps54zrcnyvB00T5w'
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Example 1
tweet = twitter.get_home_timeline()[1]
print "Tweet text: ", tweet["text"]
print "Tweet created at: ", tweet["created_at"]
print "Tweeted by: ", tweet["entities"]["user_mentions"][0]["name"]
print "Re Tweeted?: ", tweet["retweet_count"]

# Example 2
twitter.update_status(status='Testing - Twitter REST API')




