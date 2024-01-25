#Without using min() and max() functions
# num_list = [1,2,3]
def getSmallest(num_list):
    if not num_list:
        return None  
    smallest = num_list[0]

    for i in num_list:
        if i < smallest:
            smallest = i
    return smallest

    

assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None