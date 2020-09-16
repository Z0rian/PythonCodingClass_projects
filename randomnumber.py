# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:57:59 2020

@author: zorian
"""



decimals = [0.02, 0.3, 0.456]



percents = []
for i in decimals:
    percents.append(i * 100)
print(percents)


perents = [i * 100 for i in decimals]



import numpy as np
np_decimals = np.array(decimals)
np_percents = np_decimals * 100
print(np_percents)


print(np_percets.mean())
print(np_percents.me)