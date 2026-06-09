"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""

candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
final_result = []

def backtrack(start, target, temp):
    if target == 0:
        final_result.append(temp[:])
    
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i-1]:
            continue
        if candidates[i] > target:
            break
        temp.append(candidates[i])
        backtrack(start=i+1, target=target-candidates[i], temp=temp)
        temp.pop()

temp = []
backtrack(start=0, target=target, temp=temp)
print(final_result)