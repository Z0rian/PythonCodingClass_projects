# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:24:12 2020

@author: zorian
"""

def fact(n):
    n=abs(n)
    if n == 1:
        return 1
    else:
        return n * fact(n-1)



print(fact(4))
