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


#---------------------------

#time1
start1 = time.time()

matrix = np.random.randint(0, 2, size=(10000,100000))

end1 = time.time()
time1 = end1-start1
print(f'Time 1 = {time1}')
#---------------------------


#time2
start2 = time.time()

matrix = np.random.randint(0, 2, size=(10000,100000))

end2 = time.time()
time2 = end2-start2
print(f'Time 2 = {time2}')
#---------------------------


#time3
start3 = time.time()

matrix = np.random.randint(0, 2, size=(10000,100000))

end3 = time.time()
time3 = end3-start3
print(f'Time 3 = {time3}')
#---------------------------


#time4
start4 = time.time()

matrix = np.random.randint(0, 2, size=(10000,100000))

end4 = time.time()
time4 = end4-start4
print(f'Time 4 = {time4}')
#---------------------------


#time5
start5 = time.time()

matrix = np.random.randint(0, 2, size=(10000,100000))

end5 = time.time()
time5 = end5-start5
print(f'Time 5 = {time5}')
#---------------------------


#make average time and award points.
AvgTime = (time1 + time2 + time3 + time4 + time5)/5

print(AvgTime)

points = (10 - AvgTime)*10

print(f'You got {points} points!(Higher is better)')







