import numpy as np

def check_duplicate(array):
    found = False
    np_array = np.array([array]).sort()
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            found = True
            break
    
    return found

def make_unique(array):
    count = 0
    if len(array) < 3:
        return count
    
    found = check_duplicate(array)
    while(found != False):
        count = count + 1
        for i in range(0, 3):
            array.pop(i)
        if len(array) < 3:
            return count
        found = check_duplicate(array)

    return count

max_operation = make_unique([1,2,3,4,4,5,6])
print(max_operation)