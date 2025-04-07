def function1(array):
    len_ = len(array)
    i_max = []
    for i in range(1, len_, 1):
        i_max.append(max(array[i-1], array[i]))

    print(i_max)

    j_max = []
    for i in range(len_-2, -1, -1):
        j_max.append(max(array[i + 1], array[i]))

    print(j_max)


function1([2,1,4,5,3])
