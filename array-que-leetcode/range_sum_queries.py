from collections import defaultdict
def main():
    try:
        def rangeSumQueries(arr : list[int], range : list[int]) -> int: #TC: O(N)
            try:
                pref_sum = [0] * len(arr)
                curr = 0

                for i, x in enumerate(arr, start=0):
                    curr += x
                    pref_sum[i] = curr

                left, right = range
                if left == 0:
                    return pref_sum[right]
                return pref_sum[right] - pref_sum[left - 1]     

            except Exception as e:
                raise Exception(f"{str(e)}")
        sum = rangeSumQueries([1,2,3,4,5], [1,3])
        print(f"sum: {sum}")

        
    except Exception as e:
        print(f"Message: {str(e)}")

if __name__ == "__main__":
    main()