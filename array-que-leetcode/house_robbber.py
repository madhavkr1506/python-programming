def main():
    try:
        nums = [1,2,3,1]
        final_sum = bottom_up(nums=nums)
        print(f"final sum: {final_sum}")
    except Exception as e:
        print(f'Message: {str(e)}')

def recursion(nums:list) -> int: # TC: O(2^N)
    try:
        n = len(nums)
        def helper(n):
            try:
                if n == 0:
                    return nums[0]
                if n == 1:
                    return max(nums[0], nums[1])
                return max(nums[n]+helper(n-2), helper(n-1))
            except Exception as e:
                raise Exception(f"error inside helper function {str(e)}")
        return helper(n - 1)
    except Exception as e:
        raise Exception (f"failed to solve through recursion:problem: {str(e)}")
    
def top_down(nums:list) -> int: # TC: (N)
    try:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        memo = {0:nums[0], 1:max(nums[0], nums[1])}

        def helper(i):
            try:
                if i in memo:
                    return memo[i]
                else:
                    memo[i] = max(nums[i] + helper(i-2), helper(i-1))
                    return memo[i]
            except Exception as e:
                raise Exception(f"error inside helper function {str(e)}")
        
        return helper(n - 1)
        
    except Exception as e:
        raise Exception(f"failed to solve top down method\nproblem: {str(e)}")
    
def bottom_up(nums:list) -> int: # TC: (N)
    try:
        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]
        if nums == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range (2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[n-1]
        
    except Exception as e:
        raise Exception(f"failed to solve bottom up method\nproblem: {str(e)}")
    
if __name__ == "__main__":
    main()