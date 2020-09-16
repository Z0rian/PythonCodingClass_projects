# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:39:17 2020

@author: zorian
"""

words_to_scramble = ['keyboard', 'grapefruit', 'obsidion', 'person', 'camera', 'television']

#import random
from numpy import random

#randomly choose a word from list
word_choice = random.choice(words_to_scramble)

#turn word into list of charecters
char_list = list(word_choice)

#count the number of charecters in the word char_list
word_len = len(char_list)


guesses_left = 10

blanks_string = '_' * word_len
blanks_list = list(blanks_string)


while guesses_left >= 0:
    #show the status
    print (blanks_list)
    print (f'You have {guesses_left} guesses left')
    
    
    
    #ask for a letter guess
    guess = input ('Guess a letter in the word!')
    good_guess = False
    
    #find and say if the guessed letter was in the word, and if not, say so and subtract count
    for x in range(word_len):
        #print (char_list[x])
        if char_list[x] == guess[0]:
            good_guess = True
            blanks_list[x] = guess[0]
    if good_guess == False:
        guesses_left = guesses_left - 1
    
    
    
    
    #check if all the letters are guessed, and if so say end loop and say WINNN
    if blanks_list == char_list:
        print (f'You win! You made it with {guesses_left} guesses left! owo')
        break
    if guesses_left == 0:
        print ('You lose... Xd')

