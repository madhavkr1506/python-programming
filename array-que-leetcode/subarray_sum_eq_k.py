from collections import defaultdict
def main():
    try:
        # def countSubarraySum(arr : list, k : int) -> int: #TC: O(N^2)
        #     try:
        #         n = len(arr)
        #         count = 0

        #         for i in range(n):
        #             sum = 0
        #             for j in range(i, n):
        #                 sum += arr[j]
        #                 if sum == k:
        #                     count+=1
        #         return count
        #     except Exception as e:
        #         raise Exception(f"{str(e)}")
        # count = countSubarraySum([1,1,1], 2)
        # print(f"count: {count}")


        def countSubarraySum(arr : list[int], k : int) -> int: #TC: O(N)
            try:
                count = 0
                pref_count = defaultdict(int)
                pref_count[0] = 1
                curr = 0
                for x in arr:
                    curr += x
                    count += pref_count[curr-k]
                    pref_count[curr] += 1
                return count
            except Exception as e:
                raise Exception(f"{str(e)}")
        count = countSubarraySum([1,1,1], 2)
        print(f"count: {count}")

        
    except Exception as e:
        print(f"Message: {str(e)}")

if __name__ == "__main__":
    main()