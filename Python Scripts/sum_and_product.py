
def calculateSum(numbers):
    if not numbers:
        return 0  
    total = 0
    for number in numbers:
        total += number
    return total

def calculateProduct(numbers):
    if not numbers:
        return 1 
    product = 1
    for number in numbers:
        product *= number
    return product

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840