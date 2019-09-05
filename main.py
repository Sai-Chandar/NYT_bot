from Class import NYT, Twitter
import time
import os

if __name__ == '__main__':
    NYT_API = os.getenv('NYT_API')
    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
    nyt = NYT(NYT_API)
    Twitter = Twitter()
    Twitter.twitter_Authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    while True:
        mention = Twitter.mentions()
        if mention == None:
            print("waiting...")
            time.sleep(60)
            continue
        else:
            status = mention.text.lower().replace("@newyorktimesb","").strip()
            hits = "Number of NYT articles '{}' appeared: {}".format(status, nyt.frequency(status))
            tokens = Twitter.tweet(hits, mention.id)
            print("tweeted.")
        if token <= 10:
            print("Reached token limit. Waiting.")
            time.sleep(900)
