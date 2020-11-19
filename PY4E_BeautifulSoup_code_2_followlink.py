# -*- coding: utf-8 -*-

print("exercise 4 - following links in python-with test data, september 1, 2019")
#info - from week 4
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
 
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
 
url = input('Enter - ')
count = int(input("Enter count: "))+1
line_index = int(input("Enter position: ")) -1
#html = urlopen(url, context=ctx).read()
#read the entire file and return an object (soup in this case)
#soup = BeautifulSoup(html, "html.parser")
 
while count > 0 :
   html = urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
   url = tags[line_index].get("href", None)
   count = count - 1