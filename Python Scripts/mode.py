def mode(numbers):
    if not numbers:
         mode = None
    else:
        dict = {}
        for i in numbers:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
                mode = max(dict, key=dict.get)
                return mode

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4