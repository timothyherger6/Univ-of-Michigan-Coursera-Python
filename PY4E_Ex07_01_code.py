# -*- coding: utf-8 -*-
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip()
    line = line.upper()
    print(line)
# print(fh)
  