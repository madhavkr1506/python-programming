from typing import List


def main():
    try:
        nums : List[int] = [3,1,4,2]
        p : int = 6

        min_len = minSubarray(nums=nums, p=p)
        print(f"min len: {min_len}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def minSubarray(nums: List[int], p: int) -> int:  # TC: O(n) and SC: O(n)
    try:
        sum_ = sum(nums)
        if sum_ % p == 0:
            return 0
        len_ = len(nums)
        prefix_rem = {}
        prefix_rem[0] = -1

        curr = 0
        min_len = len_

        target_rem = sum_ % p
        for i, x in enumerate(nums):
            curr = (curr + x) % p
            need = (curr - target_rem + p) % p
            if need in prefix_rem:
                min_len = min(min_len, i - prefix_rem.get(need))
            prefix_rem[curr] = i

        return -1 if min_len == len_ else min_len

    except Exception as e:
        raise Exception(str(e))

if __name__ == "__main__":
    main()