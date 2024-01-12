numbers = [1,5,80,42,29,17]

sum = 0

for number in numbers:
    if number % 2 == 0:
        sum += number
print("Sum of evens = ", sum)
