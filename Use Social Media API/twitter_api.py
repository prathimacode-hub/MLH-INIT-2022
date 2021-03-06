#import necessary libraries

from google.colab import drive  # to mount Google Drive to Colab notebook
import tweepy                   # Python wrapper around Twitter API
import pandas as pd
import csv
from datetime import date
from datetime import datetime
import time

# Mounting Google Drive

drive.mount('/content/gdrive')
path = './gdrive/My Drive/'

# Load Twitter API secrets from an external file
secrets = pd.read_csv('/content/gdrive/MyDrive/secrets.csv')

consumer_key = secrets['consumer_key'][0]
consumer_secret = secrets['consumer_secret'][0]
access_token = secrets['access_token'][0]
access_token_secret = secrets['access_token_secret'][0]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Helper function to handle twitter API rate limit

def limit_handled(cursor, list_name):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("\nCurrent number of data points in list = " + str(len(list_name)))
            print('Hit Twitter API rate limit.')
            for i in range(3, 0, -1):
              print("Wait for {} mins.".format(i * 5))
              time.sleep(5 * 60)
        except tweepy.error.TweepError:
            print('\nCaught TweepError exception' )

# Helper function to get all tweets for a specified user

def user_tweets(screen_name, number_of_tweets):

  # A list to hold all tweets by tweepy
	alltweets = []	

  # To extract initial 200 tweets(most recent)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

  # Add these to the list
	alltweets.extend(new_tweets)

  # save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

  # keep grabbing tweets until we reach the desired limit
	while(len(alltweets)<number_of_tweets):
		print("getting tweets before %s" % (oldest))
	
    # all subsiquent requests use the max_id parameter to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
	
    # Add these to the list
		alltweets.extend(new_tweets)
	
    # update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	# store them as a 2D array which would later be used to write the csv file
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text, tweet.favorite_count, 
	              tweet.in_reply_to_screen_name, tweet.retweeted] for tweet in alltweets]
	
	# write the csv	
	with open(path + '%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text","likes","in reply to","retweeted"])
		writer.writerows(outtweets)
	
	pass

# Helper function to get all tweets containing a specific keyword

def keyword_tweets(search_query, number_of_tweets):

	alltweets = []	
	
	new_tweets = api.search(q=search_query,count=200)
	
	alltweets.extend(new_tweets)
	
	oldest = alltweets[-1].id - 1
	
	while(len(alltweets)<number_of_tweets):
		print("getting tweets before %s" % (oldest))
		
		new_tweets = api.search(q=search_query,count=200,max_id=oldest)
		
		alltweets.extend(new_tweets)
		
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text, tweet.favorite_count, 
	              tweet.in_reply_to_screen_name, tweet.retweeted] for tweet in alltweets]
	
	# write the csv	
	with open(path + '%s_tweets.csv' % search_query, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text","likes","in reply to","retweeted"])
		writer.writerows(outtweets)
	
	pass

# Main driver code

if __name__ == '__main__':
  choice = int(input('''Do you wish to search by:
          1. Twitter id
          2. Keyword\n'''))
  if(choice==1):
    user_id = input("Please provide the twitter id: ")
    num = int(input("Please provide the number of tweets you wish to extract (<3240): "))
    user_tweets(user_id, num)
    tweets = pd.read_csv(path + '%s_tweets.csv'%user_id)
  else:
    keyword = input("Please provide the ingredient you wish to search by: ")
    num = int(input("Please provide the number of tweets you wish to extract (<3240): "))
    keyword_tweets(keyword, num)
    tweets = pd.read_csv(path + '%s_tweets.csv'%keyword)

tweets
