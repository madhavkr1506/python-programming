import numpy as np

# time complexity: O(N log N) and space complexity: O(N)

# def check_duplicate(array):
#     found = False
#     array = sorted(array)
#     for i in range(1, len(array)):
#         if array[i] == array[i - 1]:
#             found = True
#             break
    
#     return found

# def make_unique(array):
#     count = 0
#     if len(array) < 3:
#         return count
    
#     found = check_duplicate(array)
#     while(found != False):
#         count = count + 1
#         for i in range(0, 3):
#             array.pop(0)
#         if len(array) < 3:
#             return count
#         found = check_duplicate(array)

#     return count

# max_operation = make_unique([1,2,3,4,4,5,6])
# print(max_operation)


def make_unique(nums):
    count = 0
    while(len(nums) != len(set(nums))):
        count += 1
        if(len(nums) < 3):
            nums = []
        else:
            nums = nums[3:]

    return count


print(make_unique([1,2,3,4,4,5,6]))