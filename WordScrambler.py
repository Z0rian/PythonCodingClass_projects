# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:06:30 2020

@author: zorian
Time to scramble some words?
"""

# user sees : ysk
# goal: unscramble the word to sky

words_to_scramble = ['man', 'woman', 'person', 'camera', 'television']

#import random
from numpy import random

#randomly choose a word from list
word_choice = random.choice(words_to_scramble)

#turn word into list of charecters
char_list = list(word_choice)

#1 scramble list of charecters
random.shuffle(char_list)

#2 join back as a string
scrambled_word = ''.join(char_list)
#print out the char list scrambled
print(char_list)

#3 give user a chance to guess
guess = input(f'What does {char_list} mean?')
#4 if user is correct tell them, if not let them guess again
if guess == word_choice:
    print('Nice job')
else:
    print('Wow you suck!')


###################################
#scramble list
random.shuffle(words_to_scramble)

# display scrambled list
words_to_scramble
