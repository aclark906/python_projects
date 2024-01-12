#Want the health potion to generate a random health va blue between 25 and 50 which is then applied to the starting health.
#The higher the difficulty, the less health is gained from the potion

import random

#starting health variable
health = 50
#this is a integer

difficulty = 1


potion_health = int(random.randint(25, 50) / difficulty)
#Division always creates a float. Added the cast to convert back to integer

health = health + potion_health

print(health)
