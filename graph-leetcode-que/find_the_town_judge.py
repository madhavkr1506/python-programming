def main():
    try:
        result = find_town_judge_fun()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Message: {e}")

def find_town_judge_fun():
    try:
        n = 3
        trust = [[1,3],[2,3]]
        temp_list = [0] * n
        judge = -1
        for idx in range(len(trust)):
            a, b = trust[idx]
            temp_list[a - 1] -= 1
            temp_list[b - 1] += 1
        
        for i in range(len(temp_list)):
            if temp_list[i] == n - 1:
                judge = i + 1
        return judge
    except Exception as e:
        raise e
    

# TC: O(M + N)
if __name__ == "__main__":
    main()