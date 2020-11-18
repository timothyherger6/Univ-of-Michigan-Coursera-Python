# -*- coding: utf-8 -*-
#
text = "X-DSPAM-Confidence:    0.8475";
confpos = text.find("0")
endconf = text.find("5", confpos)
confidence = text[confpos : endconf + 1]
floatconf = float(confidence)
print(floatconf) # print(confidence)