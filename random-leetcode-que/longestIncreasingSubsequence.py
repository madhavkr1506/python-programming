def main():
    try:
        array = [3, 10, 2, 1, 20]
        # max_len = recursive_approach(array=array, idx=0, prev=-10**9)
        max_len = dp_approach(array=array)
        print(f"Max len: {max_len}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def recursive_approach(array, idx, prev):
    try:
        if idx ==  len(array):
            return 0
        
        not_take = recursive_approach(array=array, idx=idx+1, prev=prev)
        take = 0
        if array[idx] > prev:
            take = 1 + recursive_approach(array=array, idx=idx + 1, prev=array[idx])

        return max(not_take, take)
        
    except Exception as e:
        raise Exception(str(e))
    
def dp_approach(array):
    try:
        n = len(array)
        dp = {}

        def solve(idx, prev_idx):
            if idx == n:
                return 0
            
            if (idx, prev_idx) in dp:
                return dp[(idx, prev_idx)]
            not_take = solve(idx+1, prev_idx)
            take = 0
            if prev_idx == -1 or array[idx] > array[prev_idx]:
                take = 1 + solve(idx+1, idx)

            dp[((idx, prev_idx))] = max(take, not_take)
            return dp[((idx, prev_idx))]
        
        return solve(0, -1)
    except Exception as e:
        raise Exception(str(e))

if __name__ == "__main__":
    main()