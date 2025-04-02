import math

# recursive approach: time complexity is O(2^n) and space complexity is O(1)

def function1(index, list1):
    if(index >= len(list1)):
        return 0
    
    include = list1[index][0] + function1(index + list1[index][1] + 1, list1)
    exclude = function1(index + 1, list1)

    return max(include, exclude) 

print(function1(0, [[2,2],[3,1],[1,4]]))


# dynamic programming approach: time complexity: O(n) and space complexity is O(n)

array_2d = [[2,2],[3,1],[1,4]]
len = len(array_2d)

def function2(array_2d, len):
    array = [0] * (len + 1)

    for i in range(0, len):
        array[i] = max(array_2d[i][0] + i + array_2d[i][1] + 1, i + 1)

