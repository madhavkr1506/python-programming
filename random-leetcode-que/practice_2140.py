import math

# recursive approach: time complexity is O(2^n) and space complexity is O(1)

def function1(index, list1):
    if(index >= len(list1)):
        return 0
    
    include = list1[index][0] + function1(index + list1[index][1] + 1, list1)
    exclude = function1(index + 1, list1)

    return max(include, exclude) 

print(function1(0, [[2,2],[3,1],[1,4]]))

def function2(list1):
    def index_helper(index):
        if(index >= len(list1)):
            return 0
        include = list1[index][0] + index_helper(index + list1[index][1] + 1)
        exclude = index_helper(index + 1)

        return max(include, exclude)

    return index_helper(0)


print(function2([[2,2],[3,1],[1,4]]))


# dynamic programming approach: time complexity: O(n) and space complexity is O(n)

array_2d = [[2,2],[3,1],[1,4]]


def function2(array_2d):
    len_ = len(array_2d)
    array = [0] * (len_ + 1)

    for i in range(len_ - 1, -1, -1):
        point, skip_index = array_2d[i]
        next_index = i + skip_index + 1
        take = point + (array[next_index] if next_index < len_ else 0)
        skip = array[i + 1]

        array[i] = max(take, skip)


    return array[0]

print(function2(array_2d))
        
