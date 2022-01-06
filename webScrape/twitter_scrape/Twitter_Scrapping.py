import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from secret import api_key, api_key_secret,access_token, access_token_secret

import tweepy as tw

auth = tw.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
query1 = "corona"
query2 = "coronavirus"
query3 = "covid"
query4 = "covid19"
# queries = ['corona','coronavirus','covid','covid19']

# get tweets from the API
tweets = tw.Cursor(api.search_tweets,
        geocode="-31.3096000,18.3570000,500km", 
        # q = [print(x) for x in queries],
        q = query1 or query2 or query3 or query4,
        lang='en',
        since = "2020-09-16").items(500)
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
print("fetched",len(tweets_copy))

import pandas as pd

# intialize the dataframe
tweets_df = pd.DataFrame()

#populate the datframe 
for tweet in tweets_copy:
    hashtags = []
    try:
        for hashtag in tweet.entities["hashtags"]:
            hashtags.append(hashtag["text"])
        text = api.get_status(id = tweet.id,tweet_mode='extended').full_text
    except:
        pass  
    tweets_df = tweets_df.append(pd.DataFrame({'username':tweet.user.name,
                                                'user_location':tweet.user.location,
                                                'user_description':tweet.user.description,
                                                'user_verified':tweet.user.verified,
                                                'date':tweet.created_at,
                                                'text':text,
                                                'hashtags': [hashtags if hashtags else None],
                                                'source': tweet.source
    
    }))

    tweets_df = tweets_df.reset_index(drop=True)
    tweets_df.to_csv('tweets.csv')



    