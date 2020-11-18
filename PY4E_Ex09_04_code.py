
# -*- coding: utf-8 -*-
# again, use mbox-short.txt or type nothing and hit enter 


# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# name = "mbox-short.txt"
# handle = open(name)
# text = handle.read()
# words = text.split()

# words = list()

# for line in handle:
#    if not line.startswith("From:") : continue
#    line = line.split()
#    words.append(line[1])


# counts = dict()

# for word in words:
#           counts[word] = counts.get(word, 0) + 1 

        
# maxval = None
# maxkey = None
# for key,val in counts.items() :
#   if maxval == None : maxval = val
#  if val > maxval:
#      maxval = val
#      maxkey = key   

# print(maxkey, maxval)

file = input("Enter file:")

if len(file) < 1:
    name = "mbox-short.txt"

fh = open(name)

from_lines = []
emails = {}

for line in fh:
    line = line.rstrip()
    if line.find('From ') == 0:
        line = line.split(' ')
        email = line[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] += 1

email = ''
count = 0

for key in emails:
    if emails[key] > count:
        count = emails[key]
        email = key

print("%s %s" % (email, str(count)))