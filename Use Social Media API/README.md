# Twitter API
## Short Description:

**Imported Libraries:**
- tweepy
- pandas
- csv


**Purpose:**
It can extract tweets from a specific user or by using a specifc keyword.

**Steps Taken:**
- Retrieved API tokens
- Added them to a `.csv` file, saved it on drive and used tokens by specifying the path
- Twitter has a rate limit of about 900 tweets/15 minutes (could vary) - an error is thrown if it's exceeded, added code to handle the error
- Created function `user_tweets` which uses api.user_timeline to extract tweets from a specific user and function `keyword_tweets`, which uses api.search to extract tweets using a search query, i.e a keyword.
- Wrote the extracted tweets in a `.csv` file, which gets created and saved in drive automatically.
- The main driver function: gave user option to choose how they wished to extract tweets and executed the code.
- Printed the hence created csv file.

------------
## Setup Instructions:
1. Get a twitter developer account by registering at [https://developer.twitter.com/en](https://developer.twitter.com/en)
2. Mount Google drive
3. Run the code.

------------

## Output:
![Covid csv file img](https://github.com/prathimacode-hub/MLH-INIT-2022/blob/main/Use%20Social%20Media%20API/Images/covid_csv.png)


------------

## References:
- [A Beginner’s Guide to Tweepy](https://towardsdatascience.com/my-first-twitter-app-1115a327349e)
  > A medium article on how to create your first Twitter App
- [Accessing the Twitter API with Python](https://stackabuse.com/accessing-the-twitter-api-with-python)
  > An introduction to the API illustrated with an example of a heat map
- [Tweepy for beginners](https://towardsdatascience.com/tweepy-for-beginners-24baf21f2c25)
  > A step-by-step guide on extracting Twitter data to create a dataset
