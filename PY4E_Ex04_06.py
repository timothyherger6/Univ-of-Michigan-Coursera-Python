# -*- coding: utf-8 -*-
#
def computepay(h,r):
    otr = r * 1.5
    pay = h * r
    paywot = ((40 * r) + ((h - 40) * otr))
    if h <= 40:
        print(pay)
    else:
        print(paywot) 
    return

hrs = input("Enter Hours:")
x = float(hrs)
rate = input("Enter Hourly Pay Rate:")
y = float(rate)
p = computepay(x, y)
# print("Pay", p)
