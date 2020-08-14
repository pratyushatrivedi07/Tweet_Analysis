import tweepy 

import sys,tweepy,csv,re

from textblob import TextBlob

import matplotlib.pyplot as plt

# Fill the X's with the credentials obtained by  

# following the above mentioned procedure. 

def percentage(part, whole):

    return 100 * float(part) / float(whole)

consumer_key = "WxrgQkoh4ow8QdFfGSDof6GIr" 

consumer_secret = "neujX45oDeet90NVTOC0MinAHbXs7k0C80jAXPuzejUSUoH8TP"

access_key = "1115498512085585920-sBevYwTPr9GxA9Oaeqq4QqWT8D1b44"

access_secret = "aHHoa0XYpgKFQPBBDAwbIZgeah39unP3b7LxrVH1iilLR"

searchTerm = input("Enter username to search about: ")


# Function to extract tweets 

def get_tweets(username): 

          

        # Authorization to consumer key and consumer secret 

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

  

        # Access to user's access key and access secret 

        auth.set_access_token(access_key, access_secret) 

  

        # Calling api 

        api = tweepy.API(auth) 

  

        # 200 tweets to be extracted 

        number_of_tweets=200

        tweets = api.user_timeline(screen_name=username, count = number_of_tweets) 

        

        

        positive = 0;

        negative = 0;

        neutral = 0;

        polarity = 0;



        for tweet in tweets:

          #print(tweet.text)

          # print(tweet.text)

          analysis = TextBlob(tweet.text)

          polarity += analysis.sentiment.polarity



          if (analysis.sentiment.polarity == 0):

              neutral += 1

          elif (analysis.sentiment.polarity < 0.00):

              negative += 1

          elif (analysis.sentiment.polarity > 0.00):

              positive += 1



        positive = percentage(positive, number_of_tweets)

        negative = percentage(negative, number_of_tweets)

        neutral = percentage(neutral, number_of_tweets)



        positive = float(format(positive, '.2f'))

        negative = float(format(negative, '.2f'))

        neutral = float(format(neutral, '.2f'))

        print(positive,negative,neutral)

        if (positive>negative and positive>neutral):

            print ('positive')

        elif (negative>positive and negative>neutral):

            print('negative')

        else:

            print('neutral')

        

        labels = ['Positive [' + str(positive) + '%]','Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]' ]

        sizes = [positive, neutral, negative]

        colors = ['yellowgreen', 'gold', 'red']

        patches, texts = plt.pie(sizes, colors=colors, startangle=90)

        plt.legend(patches, labels, loc="best")

        plt.title('How people are reacting on ' + username + ' by analyzing ' + str(number_of_tweets) + ' Tweets.')

        plt.axis('equal')

        plt.tight_layout()

        plt.show()



  

  

# Driver code 

if __name__ == '__main__': 

  

    # Here goes the twitter handle for the user 

    # whose tweets are to be extracted. 

    get_tweets(searchTerm)