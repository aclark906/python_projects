# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:23:35 2024

@author: amyro
"""

import random
        
name = input("Hello! What is your name? ").strip().capitalize()

while True:
    random_number = random.randint(1,20)
    guesses = 0
    print("Hello {}! I am thinking of a number between 1 and 20. You get 6 guesses.".format(name))
    for guesses in range(6):
        guess = input("Take a guess: ")
        guess_int = int(guess)
        if guess_int > random_number:
            print('Your guess is too high.')
            guesses = guesses + 1
        if guess_int < random_number:
            print('Your guess is too low.')
            guesses = guesses + 1
        if guess_int == random_number:
            guesses = guesses + 1
            if guesses == 1:
                print('You win! You guessed the number in ' + str(guesses) + " attempt!")
                break
            else:
                print('You win! You guessed the number in ' + str(guesses) + " attempts!")
                break
    else: 
        print('You lose! The number was ' + str(random_number) + '.')


    play_again = str(input("Do you want to play again (y/n)? ").strip().lower())
    if play_again == 'y':
        continue
    else:
        print('Thanks for playing, goodbye!')
        break
     

