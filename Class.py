import tweepy
import urllib.request, urllib.parse
import json

class NYT:
    def __init__(self, NYT_API):
        self.serviceurl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'
        self.api_key = NYT_API

    def frequency(self, q):
        self.parms = dict()
        self.parms['q'] = q
        self.parms['facet_field']='source'
        self.parms['facet']='true'
        self.parms['fq']='The New York Times'
        self.parms['api-key'] = self.api_key
        self.url = self.serviceurl + urllib.parse.urlencode(self.parms)
        print("retrieving:",self.url)
        try:
            self.data = urllib.request.urlopen(self.url).read().decode()
        except:
            return "HTTP ERROR!"
        self.info = json.loads(self.data)
        return self.info["response"]["meta"]["hits"]

class Twitter:
    api = 0
    since_id = None

    def twitter_Authentication(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        Twitter.api = tweepy.API(self.auth)

    def mentions(self, count =1):
        if Twitter.since_id == None:
            self.recent_mention = Twitter.api.mentions_timeline(count = count)
            Twitter.since_id = self.recent_mention[0].id
            return self.recent_mention[0]
        self.recent_mention = Twitter.api.mentions_timeline(since_id = self.since_id, count = count)
        #print(self.recent_mention)
        if len(self.recent_mention) == 0:
            return None
        else:
            Twitter.since_id = self.recent_mention[0].id
            return self.recent_mention[0]

    def tweet(self, status, id):
        Twitter.api.update_status(status, in_reply_to_status_id = id, auto_populate_reply_metadata = True)
        self.limits = Twitter.api.rate_limit_status()                               #returns no of tokens left for this 15 min session
        #remain_search_limits = limits['resources']['search']['/search/tweets']['remaining']
        self.remain_search_limits = self.limits['resources']['statuses']['/statuses/mentions_timeline']['remaining']
        print( "remaining tokens left for this 15 min session:", self.remain_search_limits )
        return self.remain_search_limits
