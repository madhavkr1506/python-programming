def partitionEqualSubsetSum(): # TC: O(N * Target) and SC: O(Target)
    try:
        arr : list[int] = [1,5,11,5]
        total_sum = 0
        for ele in arr:
            total_sum += ele
        print(f"Total sum: {total_sum}")
        if total_sum % 2 != 0:
            print(f"Not possible: partitionEqualSubsetSum")
        target_sum = total_sum // 2
        print(f"Target sum: {target_sum}")

        truth = [False] * (target_sum + 1)
        print(f"Truth array: {truth}")
        truth[0] = True
        print(f"Updated truth array: {truth}")

        for ele in arr:
            for a in range(target_sum, ele - 1, -1):
                # print(f"Start index: {target_sum}")
                # print(f"End index: {ele - 1}")
                # print(f"Index decrement: {-1}")
                if truth[a-ele]:
                    print(f"Element truth1: {truth[ele]}")
                    truth[ele] = True
                    print(f"Element: {ele}")
                    print(f"Element truth2: {truth[ele]}")
                    print(f"Updated truth array: {truth}")
                
        print(f"Target: {truth[target_sum]}")
                
    except Exception as e:
        print(f"Problem: {str(e)}")

if __name__ == "__main__":
    partitionEqualSubsetSum()