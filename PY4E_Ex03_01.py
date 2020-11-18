# -*- coding: utf-8 -*-
#
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Hourly Pay Rate:")
r = float(rate)
otr = r * 1.5       # overtime rate
pay = h * r         # pay if hours are less than 40
paywot = ((40 * r) + ((h - 40) * otr))     # pay if hours are greater than 40
if h <= 40:
    print(pay)
else:
    print(paywot) 