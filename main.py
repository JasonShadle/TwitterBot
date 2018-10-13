import json, config, tweepy, time, re, html,upload
# import pyodbc
from html.parser import HTMLParser

auth = tweepy.OAuthHandler(config.consumerKey, config.consumerSecret)
auth.set_access_token(config.accessToken, config.accessSecret)

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + config.server + ';DATABASE=' +
#                      config.database+';UID=' + config.username+';PWD=' + config.password)
# cursor = cnxn.cursor()


file = open('tweets.csv', 'a', encoding='utf-16')
class MyStreamListener(tweepy.StreamListener):
    loopCount = 0

    def on_status(self, status):
        if self.loopCount == 999:
            stream.disconnect()
            self.loopCount = 0

        self.loopCount += 1
        tweetID = status._json['id']
        handle = status._json['user']['screen_name']
        userID = status._json['user']['id']
        tweet = status._json['text'].replace('\n', ' ')

        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status._json['created_at'],
                                   '%a %b %d %H:%M:%S +0000 %Y'))

        if status._json['is_quote_status'] == True:
            retweet = 1
        else:
            retweet = 0

        if status._json['in_reply_to_user_id'] == None:
            reply = 0
        else:
            reply = 1
        followers = status._json['user']['followers_count']
        following = status._json['user']['friends_count']

        if status._json['user']['verified'] == False:
            verified = 0
        else:
            verified = 1
        statuses_count = status._json['user']['statuses_count']

        clean = re.compile('<.*?>')
        source = re.sub(clean, '', status._json['source'])

        # print(json_str)

        print(tweetID, handle, userID, tweet, created_at, retweet, following, followers, verified,
              statuses_count, source)
        file.write(str(tweetID) + '*!*' + handle + '*!*' + str(userID) + '*!*' + html.unescape(
            tweet) + '*!*' + created_at + '*!*' + str(retweet) + '*!*' + str(reply) + '*!*' + str(following) + '*!*' + str(
            followers) + '*!*' + str(verified) +
                   '*!*' + str(statuses_count) + '*!*' + str(source) + '\n')

    def on_error(self, status):
        print('Error: ' + str(status))
        if status == 420:
            return False
api = tweepy.API(auth)
stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
stream.filter(track=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], languages=['en'],
              stall_warnings=True)
