# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:29:48 2020

@author: zorian
"""


#asking for how many passwords it will spit out, and how long the random chars should be.
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!$%^&*,.<>/ 1234567890'
    

print('\nHello! Welcome to THE BEST Password Generator... I will prompt you with some questions, which will determine what your password looks like.\n')
print('To get started, some good awnsers are "10", for the number of passwords,')
print('"3" for the # of random charectars,')
print('"5" for how many words to choose from,')
print('and then words like your name, your pets name, and farmiliar words or phrases')
print('Here we go!')
passnum = input('How many passwords would you like to create?')
passnum = int(passnum)

#passlen = input('How many (random) charectars should the password(s) be?')
#try:
#    passlen = int(passlen)
#except ValueError:
#    print('Please put an intiger')
#    
passlen = input('How many (random) charectars should the password(s) have?')
passlen = int(passlen)
    

def randchars():
    randomsegment = ''
    for c in range(passlen):
        randomsegment += random.choice(chars)
    return randomsegment



#take a word like Zorian and turn it into Z0r1an
def leetify(inputword):
    leetword = inputword.replace('o', '0')
    leetword = leetword.replace('e', '3')
    leetword = leetword.replace('i', '1')
    leetword = leetword.replace('b', '8')
    leetword = leetword.replace('s', '5')
    leetword = leetword.replace('O', '0')
    leetword = leetword.replace('E', '3')
    leetword = leetword.replace('I', '1')
    leetword = leetword.replace('B', '8')
    leetword = leetword.replace('S', '$')
    leetword = leetword.replace('g', '&')
    leetword = leetword.replace('A', '4')
    return leetword



keywords = []

#asking how many words they want to put in. the password will still only include 2, but it will
#increase variaty.
loopsleft = input('How many words should I choose from?')
loopsleft = int(loopsleft)



#populating keywords:
while loopsleft > 0:
    word = input(f'What should the part of the password that you already know be? Number seaquence? {loopsleft} left.')
    keywords.append(word)
    keywords.append(leetify(word))
    loopsleft -= 1
    




for p in range(passnum):
    password = random.choice(keywords)
    password += randchars()
    password += random.choice(keywords)
    print(password)