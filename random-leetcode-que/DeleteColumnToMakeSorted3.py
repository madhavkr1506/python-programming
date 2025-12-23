def main():
    try:
        strs = ["babca","bbazb"]

        max_del = solution(strs=strs)
        print(f"Max del: {max_del}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def solution(strs):
    try:
        string_length = len(strs[0])
        dp = [1] * string_length

        for curr_col in range(string_length):
            for prev_col in range(curr_col):
                if all(string[prev_col] <= string[curr_col] for string in strs):
                    dp[curr_col] = max(dp[curr_col], dp[prev_col] + 1)

        return string_length - max(dp)

    except Exception as e:
        raise Exception(str(e))
    
if __name__ == "__main__":
    main()