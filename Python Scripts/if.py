import random
num1 = int(random.randint(0, 1000))
num2 = int(random.randint(0, 1000))

print("num1 = ", num1)
print("num2 = ", num2)
if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bigger than num1")
else:
    print("Both numbers are equal")
