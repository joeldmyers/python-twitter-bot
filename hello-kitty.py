#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from random import randint
# need this for random number

# argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'RV6T7NmgYOUbutp12HM4Zh9dP'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'KnqD1D82ZCVwdsVz86zaLlyfDjp31rbSCAlyA65n3mTK9FlNrb'#keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '869525080723927040-tL3BQIrAGBGR3TNogtA5CpJvL4Pkdyk'#keep the quotes, replace this with your access token
ACCESS_TOKEN_SECRET = 'aSjJ75JGwgNqaMr8knhZAd0DR6fEigFFNAJPDrsPT8Oxw'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twittersearch = api.search(q="Hello Kitty")

# print(twittersearch)
#list of specific strings we want to check for in Tweets
s = ['Hello Kitty',
    'hellokitty',
    'HelloKitty',
    'hello kitty',
    'hello kitty']


while (1 < 2):
    for stringstocheckfor in twittersearch:
        for i in twittersearch:
            if stringstocheckfor.text in i.text:
                sn = i.user.screen_name
                randnum = randint(0,2)
                print(randnum)
                if ( randnum == 0 ):
                    print('test A')
                    m = "@%s how do you do" % (sn)
                    s = api.update_status(m, i.id)
                    time.sleep(329)#Tweet every 5ish minutes
                elif ( randnum == 1 ):
                    print('test b')
                    m = "@%s hello there" % (sn)
                    s = api.update_status(m, i.id)
                    time.sleep(323)#Tweet every 5ish minutes
                else:
                    print('test c')
                    m = "@%s how's it going" % (sn)
                    s = api.update_status(m, i.id)
                    time.sleep(293)#Tweet every 5ish minutes
