import math


number = int(input('Enter a number: ').strip())
if number > 15:
    print('This system only goes up to 15 decimal places.')
else:
    print('Pi rounded to the {}th decimal is '.format(number) + str(round(math.pi, number)))
    



