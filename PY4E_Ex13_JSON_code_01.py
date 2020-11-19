# -*- coding: utf-8 -*-

import json
#import urllib
import urllib.request
#urllib must be imported ---but in python 3, urlopen is present in url.request, not just urllib
#url = raw_input("Enter location: ")
url = input('Enter - ')
#if len(url) < 1: url = "http://python-data.dr-chuck.net/comments_42.json"
if len(url) <1: url = "http://py4e-data.dr-chuck.net/comments_246369.json"
 
 
data = urllib.request.urlopen(url).read()
comments = json.loads(data)["comments"]
 
acc = 0
for comment in comments:
  acc += int(comment['count'])
 
print ("Retrieving " + url)
print ("Retrieved " + str(len(data)) + " characters")
print ("Count: " + str(len(comments)))
print ("Sum: " + str(acc))