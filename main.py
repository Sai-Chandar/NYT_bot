from Class import NYT, Twitter
import time
import os

if __name__ == '__main__':
    NYT_API = os.environ.get('NYT_API')
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
    print(type(NYT_API), CONSUMER_KEY)
    nyt = NYT(NYT_API)
    Twitter = Twitter()
    try:
        Twitter.twitter_Authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    except:
        print("Authentication error")
        exit()
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
        if tokens <= 10:
            print("Reached token limit. Waiting.")
            time.sleep(900)
