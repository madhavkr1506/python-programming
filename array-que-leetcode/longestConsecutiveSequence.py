"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

import heapq as hq

nums = [1,0,1,2]

hq.heapify(nums)

curr=0
prev=0
sequ=0
maxs=0
for i in range(len(nums)):
    if i==0:
        curr=hq.heappop(nums)
        sequ=1
        prev=curr
    else:
        curr=hq.heappop(nums)
        print(curr, prev)
        if curr-prev==1:
            sequ+=1
            maxs = max(maxs, sequ)
            prev=curr
        elif prev==curr:
            continue
        else:
            sequ=1
            prev=curr

print(maxs)
