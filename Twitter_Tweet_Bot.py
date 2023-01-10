# imported modules
import schedule 
import time 
import openai, tweepy, random

# Initialization
api_key  =""
api_key_secret =""
access_token=""
access_token_secret=""



### TWEET ###
def func():
   class TwitterBot():
      #OpenAI
      openai.api_key = "Insert OpenaAI API Key"
      #Initialization 1 
      auth = tweepy.OAuthHandler(api_key, api_key_secret)
      auth.set_access_token(access_token, access_token_secret)
      api = tweepy.API(auth, wait_on_rate_limit=True)
      # Creating Tweets with keywords
      prompts = [
         {
            "hashtag": "",
            "text": "Tell something funny"
         },
         {
            "hashtag": "",
            "text": "Tell a Joke"
         },


                 
      ]
      def __init__(self):
         error = 1
         while(error == 1):
            tweet = self.create_tweet()
            try:
               error = 0
               self.api.update_status(tweet)
               print(tweet)
            except:
               error = 1
      def create_tweet(self):
         chosen_prompt = random.choice(self.prompts)
         text = chosen_prompt["text"]
         hashtags = chosen_prompt["hashtag"]

         response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=text,
            max_tokens=64,
         )

         tweet = response.choices[0].text
         tweet = tweet + " " + hashtags
         return tweet

   twitter = TwitterBot()
   twitter.create_tweet()
schedule.every(15).minutes.do(func)
while True:
    schedule.run_pending()
    time.sleep(15)

