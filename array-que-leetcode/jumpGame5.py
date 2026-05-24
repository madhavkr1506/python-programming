class ListException(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class EmptyListException(ListException):
    pass

def maxJumps(arr:list[int], d:int)->int:
    try:
        n1 = len(arr)
        if n1==0: raise EmptyListException(f"list of length zero")
        dp = [-1]*n1
        max_index_visit = 0
        for i in range(n1):
            max_index_visit = max(max_index_visit, helper(arr=arr, index=i, d=d, dp=dp))
        return max_index_visit

    except Exception as err:
        if isinstance(err, EmptyListException):
            raise err
        raise err
    
def helper(arr:list[int], index:int, d:int, dp:list[int])->int:
    if dp[index]!=-1:
        return dp[index]
    
    ans = 1
    
    # left
    for step in range(1, d+1):
        next = index - step
        if next < 0:
            break
        if arr[next] >= arr[index]:
            break
        explore_left = helper(arr=arr, index=next, d=d, dp=dp)
        ans=max(ans, 1+explore_left)

    # right
    for step in range(1, d+1):
        next = index + step
        if next >= len(arr):
            break
        if arr[next] >= arr[index]:
            break
        explore_right = helper(arr=arr, index=next, d=d, dp=dp)
        ans=max(ans, 1+explore_right)

    dp[index] = ans
    return dp[index]

"""
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and  0 < x <= d.
i - x where: i - x >= 0 and  0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
Example 1:
Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 105
1 <= d <= arr.length
 


"""

def main():
    try:
        arr = [7,6,5,4,3,2,1]
        d = 1
        max_index_visit = maxJumps(arr=arr, d=d)
        print(f"max index visit: {max_index_visit}")
    except Exception as err:
        if isinstance(err, EmptyListException):
            print(f"empty list exception: {str(err)}")
            return
        print(f"generic exception: {str(err)}")


if __name__ == "__main__":
    main()