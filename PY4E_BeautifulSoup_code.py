# -*- coding: utf-8 -*-

print("exercise 3 - Exploring the HyperText Transport Protocol")
#screen scrape example - from week 4
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
html = urlopen(url, context=ctx).read()
#read the entire file and return an object (soup in this case)
soup = BeautifulSoup(html, "html.parser")
#tags <th> defines a header cell, <tr> defines a row in a table; <td> defines a cell in a table
#the span tag does some style change within its realm <span>  </span>
 
# Retrieve all of the <span> tags in the file and pull out the numbers fromt he tag and sum the numbers.
# <td>Name</td><td>Comments</td>
# </tr>
# <tr><td>Romina</td><td><span class="comments">97</span></td></tr>
#<span class="comments">97</span>  ---> class is comments, span means
value=0
summation=0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    ##print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    value = int(tag.contents[0])
    print("value", value)
    summation = value + summation
print("summation = ", summation)
#files to test the code
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_246366.html (Sum ends with 38)