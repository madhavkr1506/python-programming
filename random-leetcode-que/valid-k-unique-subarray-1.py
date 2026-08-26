

"""
You are given an integer array nums and an integer k.

You are also given a 2D integer array queries, where queries[i] = [li, ri] represents the subarray nums[li..ri].

For each query, the subarray nums[li..ri] is considered valid if:

It contains exactly k distinct numbers, and
The frequency of every number in the subarray is even.
Return a boolean array ans, where ans[i] is true if nums[li..ri] is valid, and false otherwise.

 

Example 1:

Input: nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]

Output: [false,true,false]

Explanation:

i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
0	[0, 1]	[1, 2]	{1, 2} → 2	{1: 1, 2: 1}	false: Element counts are not even.
1	[0, 3]	[1, 2, 2, 1]	{1, 2} → 2	{1: 2, 2: 2}	true: Exactly k = 2 distinct elements, all appear an even number of times.
2	[1, 2]	[2, 2]	{2} → 1	{2: 2}	false: Number of distinct elements is less than k = 2.
Thus, ans = [false, true, false].

Example 2:

Input: nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]

Output: [true,false]

Explanation:

i	[li, ri]	Subarray	Unique numbers	Frequency	Validity check
0	[1, 2]	[3, 3]	{3} → 1	{3: 2}	true: Exactly k = 1 distinct element, appears an even number of times.
1	[0, 2]	[3, 3, 3]	{3} → 1	{3: 3}	false: 3 does not appear an even number of times.
Thus, ans = [true, false].

 

Constraints:

2 <= n == nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= n
1 <= queries.length <= 105
queries[i] == [li, ri]
0 <= li < ri <= n - 1

"""

nums = [1,2,2,1]
k = 2
queries = [[0,1],[0,3],[1,2]]
ans = []

# for start, end in queries:
#     freq_map = {}
#     for idx in range(start, end+1):
#         freq_map[nums[idx]] = freq_map.get(nums[idx], 0) + 1
#     print(f"Frequency map: {freq_map}")
#     odd_found = False
#     distinct_ele = set()
#     for key, value in freq_map.items():
#         distinct_ele.add(key)
#         if value % 2 == 1:
#             odd_found = True
#     if odd_found: ans.append(False)
#     else: 
#         if len(distinct_ele) != k: ans.append(False)
#         else: ans.append(True)


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def prefix_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)
    
    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

import random

n = len(nums)
q = len(queries)

rand_val = {}

def get_rand(x):
    if x not in rand_val:
        rand_val[x] = random.getrandbits(64)
    return rand_val[x]

prefix_xor = [0] * (n + 1)

for i in range(n):
    prefix_xor[i+1] = prefix_xor[i] ^ get_rand(nums[i])

prev = [-1] * n 
last_seen = {}

fen = Fenwick(n)

queries_by_r = [[] for _ in range(n)]

for q_idx, (left, right) in enumerate(queries):
    queries_by_r[right].append((left, q_idx))

distinct_count = [0] * q

for idx, num in enumerate(nums):
    if num in last_seen:
        prev[idx] = last_seen[num]
    if prev[idx] != -1:
        fen.update(prev[idx], -1)
    fen.update(idx, 1)
    last_seen[num] = idx
    for (l, q_idx) in queries_by_r[idx]:
        distinct_count[q_idx] = fen.range_sum(l, idx)

print(f"Previous index: {prev}")
for q_idx, (l, r) in enumerate(queries):
    even_ok = (prefix_xor[r + 1] == prefix_xor[l])
    distinct_ok = (distinct_count[q_idx] == k)
    ans.append(bool(even_ok and distinct_ok))

print(f"Answer: {ans}")