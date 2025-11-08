from collections import defaultdict
def main():
    try:
        def rangeUpdate(arr : list[int], upg_range : list[int], delta : int) -> list[int]: #TC: O(N)
            try:
                n = len(arr)
                left, right = upg_range
                diff_arr = [0] * (n + 1)
                if right + 1 < n:
                    diff_arr[right] -= delta
                diff_arr[left] += delta

                print(f"difference array: {diff_arr}")

                res_arr = [0] * n
                curr = 0

                for i, x in enumerate(arr, start=0):
                    curr += diff_arr[i]
                    res_arr[i] = arr[i] + curr
                return res_arr
            except Exception as e:
                raise Exception(f"{str(e)}")
        list_ = rangeUpdate([1,2,3,4,5], [1,3], 3)
        print(f"list: {list_}")

        
    except Exception as e:
        print(f"Message: {str(e)}")

if __name__ == "__main__":
    main()