#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
from time import sleep

from retweetingstreamlistener import RetweetingStreamListener
from tokens import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def setup_api():
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  return tweepy.API(auth)


if __name__ == '__main__':
	api = setup_api()

	while True:
		stream = tweepy.Stream(auth = api.auth, listener=RetweetingStreamListener(api))
		stream.filter(track=['#zaunei2016', '@zaunei2016'])
		print("[Error] Something went wrong reconnecting")
		sleep(10.0)
