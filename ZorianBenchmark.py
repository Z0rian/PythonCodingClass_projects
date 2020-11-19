# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:33:09 2020

@author: zorian
"""

 # Import numpy to handle matrices
import numpy as np

# Generates random 2 by 3 matrix
matrix = np.random.rand(2,3)
matrix

import pandas as pd
df = pd.DataFrame(matrix)
df

df.iloc[1, 2]
matrix[1, 2]

# 1D random number between 0 and 1
matrix = np.random.randint(0, 2)

matrix = np.random.randint(0, 2, size=(2,3))

matrix = np.random.randint(0, 2, size= (20,30))

# Computes average times


import time
time.time()


times = []

repeats = 5

#---------------------------
def benchmatrix():
    start1 = time.time()
    matrix = np.random.randint(0, 2, size=(10000,100000))
    end1 = time.time()
    time1 = end1-start1

    
    return time1



for n in range(repeats) :
    times.append(benchmatrix())
    print(f'Time {len(times)} = {times[-1]}')
    
    
    
    


#make average time and award points.
AvgTime = (sum(times)/len(times))

print(AvgTime)

points = (10 - AvgTime)*10

print(f'You got {points} points!(Higher is better)')







