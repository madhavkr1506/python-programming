def coinChangeTwo():
    try:
        amount = 5
        coins = [1,2,5]
        print(f"Amount: {amount}")
        print(f"Coins: {coins}")

        dp = [0] * (amount + 1)
        print(f"DP: {dp}")
        dp[0] = 1
        print(f"DP: {dp}")

        for coin in coins:
            for a in range(coin, amount + 1):
                print(f"Before {dp[a]}")
                dp[a] = dp[a] + dp[a - coin]
                print(f"After {dp[a]}")
                print(f"DP: {dp}")
        print(f"Outside loop")
        print(f"DP: {dp}")

    except Exception as e:
        print(f"Problem: {str(e)}")
    
if __name__ == "__main__":
    coinChangeTwo()