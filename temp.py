# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


orange_sky = True

while True:
    print('The Sky is Orange.')
    color = input('Choose a color of sky')
    if color.lower() != 'orange':
        orange_sky = False
print(f'The color of sky is {color}')