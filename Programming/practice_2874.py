import math

def function1(array):
    len_ = len(array)
    i_max = [0] * len_
    i_max[0] = (array[0])
    for i in range(1, len_, 1):
        i_max[i] = (max(i_max[i-1], array[i]))


    j_max = [0] * len_
    j_max[-1] = array[-1]
    for j in range(len_-2, -1, -1):
        j_max[j] = (max(j_max[j + 1], array[j]))

    max_value = -math.inf
    for i in range(1, len_ - 1, 1):
        max_value = max((i_max[i - 1] - array[i]) * j_max[i + 1], max_value)

    print(max_value)




function1([12,6,1,2,7])
