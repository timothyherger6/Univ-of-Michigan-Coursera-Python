# -*- coding: utf-8 -*-
# use romeo.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
# print(line.rstrip())
# print(sortwords)
lst.sort()
print(lst)     