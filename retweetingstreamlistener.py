#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import tweepy

# Nothing wrong with a nice enterprisy class name, right?
class RetweetingStreamListener(tweepy.StreamListener):


	def on_status(self, status):
		print "[Info] %s - %s" % (status.user.screen_name, status.text)

		if not hasattr(status, 'retweeted_status'):
			status.retweet()
			print "[Info] Retweeted!"


		print "-----------------------------------------"


	def on_error(self, status_code):
		# Rate limiting
		if status_code == 420:
			print "[Error] Got Error 420, rate limiting in effect"
			#returning False in on_data disconnects the stream
			return False

		print "[Error] Got status code %d" % status_code
