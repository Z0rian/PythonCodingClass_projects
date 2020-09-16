# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:32:33 2020

@author: zorian
User inputs radius, outputs is area, circumference of circle
"""



#get User input
radius = input('Choose a radius')
radius = float(radius)


def area(rad):
    return rad ** 2 *3.141592653579

def volume(vol):
    return vol **2 * 3.141592653579 * 4


user_area = area(radius)
user_volume = volume(radius)



print(f'the area of a circle with radius of {radius} is {user_area}.')
print(f'the volume of a sphere with a radius of {radius} is {user_volume}.')
