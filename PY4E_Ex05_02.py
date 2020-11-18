# -*- coding: utf-8 -*-
#
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        fnum = float(num)
        inum = int(fnum)
    except:
        print('Invalid input')
    
    if smallest is None:
        smallest = inum
    elif fnum < smallest:
        smallest = inum
    if largest is None:
        largest = inum
    elif fnum > largest:
        largest = inum    
        
print("Maximum is", largest)
print("Minimum is", smallest)