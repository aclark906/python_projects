# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 13:18:30 2024

@author: amyro
"""




    
temperature = float(input("What is the temperature? "))
print(temperature)

unit = input("Is this in Fahrenheit or Celsius? ").strip().lower()

fahrenheit = temperature * (9 / 5) + 32

celsius = (temperature - 32) * (5 / 9)

if unit.startswith("c"):
    print("A temperature of " + str(temperature) + " Celsius is " + str(fahrenheit) + ' Fahrenheit.')
else:
    print("A temperature of " + str(temperature) + " Fahrenheit is " + str(celsius) + ' Celsius.')
