from flask import render_template, url_for, redirect, flash, send_from_directory, request
from datatreasure import datatreasure
from keys import one, two, three, four
import os
import tweepy
import re
import json

@datatreasure.route('/')
@datatreasure.route('/home')
@datatreasure.route('/home/')

def index():
    return render_template("home.html")

@datatreasure.route('/search', methods=['POST'])

def search():
    keyword = request.form['keyword']

    auth = tweepy.OAuthHandler(one, two)
    auth.set_access_token(three, four)

    api = tweepy.API(auth)

    hashtag = list()

    for tweet in tweepy.Cursor(api.search, q=keyword, count=100, lang="en").items(100):
    	temp = re.findall(r'#\w+', tweet.text)
    	if temp:
    		for i in temp:
    			hashtag.append(i)
    	else:
    		pass

    print hashtag
    str = ""
    for i in hashtag:
        str += i + " "

    return str
