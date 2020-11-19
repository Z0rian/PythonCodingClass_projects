# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 10:17:52 2020

@author: zorian
"""

#create a dictionary of primes, prime squares, prime cubes
prime_list= [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43, 47]


prime_dict = {'primes': [2, 3, 5, 7, 11, 13, 17, 19],
              'prime_square': [p**2 for p in prime_list],
              'prime_cubes' : [p**3 for p in prime_list]}


print(prime_dict)

import pandas as pd

df = pd.DataFrame(prime_dict)

df.describe()
import matplotlib.pyplot as plt
plt.hist(['prime_squares'])
plt.show
