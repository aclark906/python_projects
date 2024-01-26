def median(numbers):

    if not numbers:
        median = None 
    numbers.sort()
    for i in range(len(numbers)):
        if len(numbers) % 2 == 0:
            num_1 = numbers[(len(numbers) // 2) - 1]
            num_2 = numbers[len(numbers) // 2]
            median = (num_1 + num_2) / 2
        else:
            median = numbers[int(len(numbers) / 2)]
    return median


assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6