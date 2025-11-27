from typing import List


def main():
    try:
        nums : List[int] = [1,2]
        k : int = 1

        bestCandidate = maxSubarraySum(nums=nums, k=k)

        print(f"final answer: {bestCandidate}")
        
    except Exception as e:
        print(f"Problem: {str(e)}")

def maxSubarraySum(nums: List[int], k: int) -> int:
    if k == 0:
        raise Exception(f"zero division")
    
    prefixSum = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        prefixSum[i] = prefixSum[i-1] + nums[i-1]

    inf = 10**30
    minPref = [inf] * k

    minPref[0] = 0
    best = -10**30

    for i in range(1, len(nums) + 1):
        r = i % k
        if minPref[r] != inf:
            candidate = prefixSum[i] - minPref[r]
            if candidate > best:
                best = candidate
        if prefixSum[i] < minPref[r]:
            minPref[r] = prefixSum[i]

    return best 

if __name__ == "__main__":
    main()