# Tweet_Analysis

This work was done for a course project.

## About the Project
For a given username it classifies whether the reactions of the public on the tweets posted by that particular username is of positive, negative, or neutral sentiment.

You don't need a dataset. We are using Tweepy (a Twitter API) for accessing the tweets. Then we will perform the analysis on those tweets.

## Requirements
There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.
- `tweepy`
- `sys`
- `csv`
- `re`
- `matplotlib`
- `textblob`

## Setting up the environment
### Step 1: Tweepy Account
To be able to retrieve data using Tweepy you are going to need the following things:
- Install `tweepy module`.
- You can execute the command `pip install tweepy` in the command-line to install it.
- Create an app in [Twitter Developers](https://apps.twitter.com/). 
- An authenticated Twitter user is required.
- Create an `access token`. You can achieve that by accessing the *`Keys and AccessToken tab`* of your Twitter App’s main page and clicking in Create my access token
button.

###  Step 2: Accessing the API using tweepy
First, we need to import the tweepy module

``import tweepy``

Now we are going to need to set the variables that are required to initially have access to the Twitter API. They are the Consumer Key, Consumer Secret, Access Token and Access Token
Secret. 
You have access to all their values in in *`App's Manage Keys and Access Token tab`* in the App's main page.
```
consumer_key = "Your Consumer Key";
consumer_secret = "Your Consumer Secret";
access_token = "Your Access Token";
access_token_secret = "Your Access Token Secret";
```

Now we set ``OAuth authentication`` to allow tweepy to connect to Twitter API. 
To achieve that, we are going to create a `tweepy.OAuthHandler` instance and pass both Consumer Key and Consumer Secret as parameters, in this order. Also it is needed to call the
``OAuthHandler.set_access_token`` method passing both Access Token and Access Secret as parameters. Finally, we instantiate the `tweepy.API` class passing the `OAuthHandler` instance
we have created as parameter.
```
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```
## Running the Code
Make sure you have all the requirements installed.

Run the code using:
``` python3 tweet.py ``` or ```python tweet.py ```
