"""
You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

Constraints:

1 <= intevals.length <= 5 * 104
intervals[i].length == 3
intervals[i] = [li, ri, weighti]
1 <= li <= ri <= 109
1 <= weighti <= 109
"""

intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

from dataclasses import dataclass

@dataclass(frozen=True)
class T:
    weight: int
    selected: tuple[int]

    def __iter__(self):
        yield self.weight
        yield self.selected


import math
import functools
import bisect

def solution(intervals) -> list[int]:

    intervals = sorted((*interval, i) for i, interval in enumerate(intervals))

    @functools.lru_cache(maxsize=None)
    def dp(i:int, k:int) -> T:

        if i == len(intervals) or k == 0:
            return T(0, ())
        skip = dp(i + 1, k)
        _, r, weight, original_idx = intervals[i]
        j = bisect.bisect_right(intervals, (r, math.inf))
        next_res = dp(j, k - 1)
        pick = T(weight + next_res.weight, sorted((original_idx, *next_res.selected)))
        return (
            pick 
            if pick.weight > skip.weight or pick.weight == skip.weight and pick.selected < skip.selected
            else
            skip
        )

    return list[dp(0, 4).selected]


print(solution(intervals=intervals))





