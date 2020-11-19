# -*- coding: utf-8 -*-
# now, this time, use regex_sum_245868.txt or type nothing and hit enter   

print("exercise 2 - using regular expressions")
 
 
 
import re
 
 
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_245868.txt"
fh = open(fname)
num_sum = list()
count=0
for line in fh:
    print(line)
    line=line.rstrip()
    #line = line.translate(str.maketrans(",",string.punctuation)
    stuff=re.findall('[0-9]+' , line)
    print("stuff=",stuff)
    for i in range (len(stuff)):
        stuff[i]=int(stuff[i])
        count=count + stuff[i]
        print("count=", count)
print(count)