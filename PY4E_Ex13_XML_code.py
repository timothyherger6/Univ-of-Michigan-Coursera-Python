# -*- coding: utf-8 -*-

print("exercise 5 - Extracting data from XML (chapter 13)")
 
import urllib.request
 
import xml.etree.ElementTree as ET
 
#url = raw_input("Enter location: ")
url = input('Enter - ')
if len(url) < 1:
    #url = " http://py4e-data.dr-chuck.net/comments_42.xml"---> test data
    url=  "http://py4e-data.dr-chuck.net/comments_246368.xml"
print ("Retrieving " + url)
 
xml = urllib.request.urlopen(url).read()
print ("Retrieved: " + str(len(xml)) + " characters")
 
tree = ET.fromstring(xml)
 
counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))
 
accumulator = 0
 
for count in counts:
    accumulator += int(count.text)
 
print ( "Sum:" + str(accumulator))