def coinChange1():
    try:
        coins : list[int] = [1,2,5]
        amount = 11
        print(f"Coins : {coins}")
        print(f"Amount: {amount}")

        dp = [float('inf')] * (amount + 1)
        print(f"DP: {dp}")
        dp[0] = 0
        
        for coin in coins:
            for a in range(coin, amount+1, 1):
                print(f"dp[a]1: {dp[a]}")
                dp[a] = min(dp[a], 1 + dp[a-coin])
                print(f"dp[a]2: {dp[a]}")
        print(f"dp[amount]: {dp[amount]}")
    except Exception as e:
        print(f"Problem: {str(e)}")

if __name__ == "__main__":
    coinChange1()