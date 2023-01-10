# imported modules
import time 
import tweepy
from textblob import TextBlob

# Initialization
api_key  =""
api_key_secret =""
access_token=""
access_token_secret=""

mention_id = 1

### LIKE ###
while True:
    # Initialization
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #like
    mentions = api.mentions_timeline(since_id = mention_id)
    for mention in mentions:
        print(f"Mention Tweet Found!")
        print(f"Mention: {mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        mention_analysis = TextBlob(mention.text)
        mention_analysis_score = mention_analysis.sentiment.polarity
        print(f"Tweet has polarity score of {mention_analysis_score}")
        if mention_analysis_score >=0.3 and not mention.retweeted:
            try:
                    print('trying to like ..------------')
                    api.create_favorite(mention.id)
                    print("Tweet successfully liked")
            except Exception as err:
                    print(err)
        else:
                print("Tweet will not be liked")
    time.sleep(15)