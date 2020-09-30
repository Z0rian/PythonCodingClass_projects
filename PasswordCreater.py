# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:29:48 2020

@author: zorian
"""

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*,.<>/;:-_=+`~'
    
passnum = input('How many passwords would you like to create?')
passnum = int(passnum)

passlen = input('How many (random) charectars should the password(s) be?')
passlen = int(passlen)

loopsleft = 5




for p in range(passnum):
    password = ''
    for c in range(passlen):
        password += random.choice(chars)
    print(password)
    
    
    while loopsleft => 0:
        passpart = input(f'What should the part of the password that you already know be? Pet name, favorate food? {loopsleft} left.')
        passpart = int(passpart)
        password.append(passpart)
        