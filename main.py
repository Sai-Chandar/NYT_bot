from hidden import *
from Class import NYT, Twitter
import time

if __name__ == '__main__':
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
            status = mention.text.replace("@Nsaichandar","").strip()
            hits = "Number of NYT articles '{}' appeared: {}".format(status, nyt.frequency(status))
            Twitter.tweet(hits, mention.id)
            print("tweeted.")
