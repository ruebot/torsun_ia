#!/usr/bin/env python

import tweepy
import robotparser
import config
import time

auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_KEY, config.TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

rp = robotparser.RobotFileParser()
rp.set_url("http://www.torontosun.com/robots.txt")
torsun_ia = rp.can_fetch("ia_archiver", "http://www.torontosun.com/")
today = time.strftime("%Y-%m-%d")

if torsun_ia == False:
    text = "The Internet Archive is still not allowed to crawl @TheTorontoSun.\n\nSee: http://www.torontosun.com/robots.txt\n\n'Disallow ia_archive'\n\n"
    tweet_text = "%s%s" % (text, today)
    api.update_status(tweet_text)
if torsun_ia == True:
    text = "The Internet Archive is now allowed to crawl @TheTorontoSun! / @ruebot\n"
    tweet_text = "%s%s" % (text, today)
    api.update_status(tweet_text)
