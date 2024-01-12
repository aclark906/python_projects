# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:44:40 2024

@author: amyro
"""

import random
import time

intro = '''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.'''

responses = ['Gobbles you down in one bite! You lose!',
             '''Offers you his treasure! You win!
             *     
            * *
           *   *
          *     *
         *       *
          *     *
           *   *
            * *
             *
             ''']



pick = ''
while True:
    while pick != "1" and pick != "2":
        print(intro)    
        random_number = random.randint(1,2)
        pick = input('Which cave will you go into (1 or 2)? ')
    if pick == "1" or pick == "2":
        print('You approach the cave...')
        time.sleep(2)
        print('It is dark and spooky...')
        time.sleep(2)
        print('A large dragon jumps out in front of you!') 
        time.sleep(2)     
        print('He opens his jaws and...')
        time.sleep(5)
        print(random.choice(responses))
    play_again = str(input("Do you want to play again (y/n)? ").strip().lower())
    if play_again.startswith('y'):
        pick = input('Which cave will you go into (1 or 2)? ')
    else:
        print('Thanks for playing, goodbye!')
        break
