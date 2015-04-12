from collections import Counter
from flask import render_template, url_for, redirect, jsonify, request
from datatreasure import datatreasure
from keys import one, two, three, four
import os
import tweepy
import re
import json
import random

chars = '0123456789ABCDEF'

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
    num = 500
    hashtag = list()

    for tweet in tweepy.Cursor(api.search, q=keyword, count=num, lang="en").items(num):
    	temp = re.findall(r'#\w+', tweet.text)
    	if temp:
    		for i in temp:
    			hashtag.append(i[1:].lower())
    	else:
    		pass

    d = {}
    [d.__setitem__(item,1+d.get(item,0)) for item in hashtag]

    if keyword.lower() in d:
        del d[keyword.lower()]

    for i in d.keys():
        if d[i] < 10:
            del d[i]

    content = list()
    for i in d.keys():
        temp = {}
        temp["datLabel"] = i
        temp["value"] = d[i]
        #temp["color"] = ['#'+''.join(sample(chars,6)) for i in range(6)]
        temp["color"] = "#0C9F8F"
        content.append(temp)

    print json.dumps(content)

    return render_template("view.html", jsonStr=json.dumps(content), keyword=keyword, num=num)

@datatreasure.route("/data", methods=['POST'])
def data():
    glob = request.form['glob']
    print "DATA", glob
    temp = {}
    temp["data"] = glob
    return jsonify(temp)
