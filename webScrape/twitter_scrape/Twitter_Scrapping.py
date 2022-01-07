import sys
import tweepy
import matplotlib.pyplot as plt
import numpy as np
from secret import api_key, api_key_secret,access_token, access_token_secret
import tweepy
from tweepy.auth import OAuthHandler
from tweepy import API
import pandas as pd

class Scrape_twitter:
    def get_access(self):
        auth = OAuthHandler(api_key,api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = API(auth, wait_on_rate_limit=True)
        return api

    def get_tweets(self):
        self.get_access()
        query1 = "corona"
        query2 = "coronavirus"
        query3 = "covid"
        query4 = "covid19"
        query5 = "lockdown"
        query6 = "Covid_19"
        query7 = 'omicron'

        # get tweets from the API
        tweets = tweepy.Cursor(self.get_access().search_tweets,
                geocode="-31.3096000,18.3570000,500km", 
                # q = [print(x) for x in queries],
                q = query1 or query2 or query3 or query4 or query5 or query6 or query7,
                lang='en',
                since = "2020-09-16").items(500)
        tweets_copy = []
        for tweet in tweets:
            tweets_copy.append(tweet)
        print("fetched",len(tweets_copy))

        return tweets_copy

    def get_data(self):
        tweets_df = pd.DataFrame()
        #populate the datframe 
        tweets_copy = self.get_tweets()

        for tweet in tweets_copy:
            hashtags = []
            try:
                for hashtag in tweet.entities["hashtags"]:
                    hashtags.append(hashtag["text"])
                text = self.get_access().get_status(id = tweet.id,tweet_mode='extended').full_text
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



if __name__ == '__main__':
    tw = Scrape_twitter()
    print(tw.get_data())
