numbers = range(1,501)
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("even numbers", even)
print("odd numbers", odd)
