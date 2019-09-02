from hidden import *
from Class import NYT, Twitter

if __name__ == '__main__':
    nyt = NYT(NYT_API)
    Twitter = Twitter()
    Twitter.twitter_Authentication(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    mention, id = Twitter.mentions()
    mention = mention.replace("@Nsaichandar","").strip()
    hits = nyt.frequency(mention)
    Twitter.tweet(hits,id)
