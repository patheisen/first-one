# -*- coding: utf-8 -*-
"""
Created on Fri May  4 00:13:07 2018

@author: paul
"""

okchar = "hlc"
info = "a"
low = 0
high = 100
guess = int((low+high)/2)

print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(guess) + ' ?' )

info = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')

while info != 'c':
    if info not in okchar:
        print("Sorry, I did not understand your input.")
        print('Is your secret number ' + str(guess) + ' ?' )
        info = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ') 
    elif info == 'l':
        low = guess
        guess = int((low+high)/2)
        print('Is your secret number ' + str(guess) + ' ?' )
        info = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')
    elif info == 'h':
        high = guess
        guess = int((low+high)/2)
        print('Is your secret number ' + str(guess) + ' ?' )
        info = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ')
print('Game over. Your secret number was: ' + str(guess))