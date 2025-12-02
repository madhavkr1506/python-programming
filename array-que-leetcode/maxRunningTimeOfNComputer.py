from typing import List


def main():
    try:
        n = 2
        batteries = [1,1,1,1]

        maxtime = maxRunTime(n=n, batteries=batteries)
        print(f"maxtime: {maxtime}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def maxRunTime(n: int, batteries: List[int]) -> int:
    try:
        if not 1 <= n <= 10**5:
            raise Exception(f"out of range n")
        
        low = 0
        high = sum(batteries) // 2

        while(low < high):
            mid = (low + high + 1) // 2
            curr_cap = sum(min(cap, mid)for cap in batteries)
            if curr_cap >= n * mid:
                low = mid
            else:
                high = mid - 1
        return low
    except Exception as e:
        raise Exception(str(e))


if __name__ == "__main__":
    main()