import json, config, tweepy, pyodbc, time

auth = tweepy.OAuthHandler(config.consumerKey, config.consumerSecret)
auth.set_access_token(config.accessToken, config.accessSecret)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + config.server + ';DATABASE=' +
                      config.database+';UID=' + config.username+';PWD=' + config.password)
cursor = cnxn.cursor()


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        tweetID = status._json['id']
        handle = status._json['user']['screen_name']
        userID = status._json['user']['id']
        tweet = str(['text'])
        if status._json['coordinates'] != None:
            coordinates = str(status._json['coordinates']).split(',')
            long = coordinates[0]
            lat = coordinates[1]
        else:
            long = None
            lat = None
        created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status._json['created_at'],
                                   '%a %b %d %H:%M:%S +0000 %Y'))
        lang = status._json['lang']

        if status._json['is_quote_status'] == True:
            retweet = 0
        else:
            retweet = 1
        followers = status._json['user']['followers_count']
        following = status._json['user']['friends_count']

        if status._json['user']['verified'] == False:
            verified = 0
        else:
            verified = 1
        statuses_count = status._json['user']['statuses_count']




            # json_str = json.dumps(status._json)
            # print(json_str)

    def on_error(self, status):
        print('Error: ' + str(status))
        if status == 420:
            return False

api = tweepy.API(auth)
listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)
stream.filter(track=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], languages=['en'])
