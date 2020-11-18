# -*- coding: utf-8 -*-
# use mbox-short.txt as the file name or just type nothing and hit enter 
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') : 
        continue
    else : 
        count = count + 1
        words = line.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
