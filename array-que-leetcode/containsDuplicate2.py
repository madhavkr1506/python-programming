
class EmptyListException(Exception):
    def __init__(self, message : str):
        super().__init__(message)

class EmptyList(EmptyListException):
    pass

def containsNearbyDuplicate(nums: list[int], k: int)-> bool:
    try:
            n1 = len(nums)
            lookup = {}
            if n1 == 0: raise EmptyListException(f"empty list has been identified")
            for left in range(n1):
                if nums[left] in lookup:
                    if abs(lookup[nums[left]] - left) <= k: return True
                lookup[nums[left]] = left 
                # right = left+1
                # while right < n1 and abs(left - right) <= k:
                #     if nums[left] == nums[right] and abs(left - right) <= k:
                #         return True
                #     right += 1
            return False
    except EmptyListException as ele:
        raise ele
    except Exception as e:
        raise Exception(f"execution failure: {str(e)}")
    
def main():
    try:
        nums = [1,2,3,1,2,3]
        k = 2
        bool_flag = containsNearbyDuplicate(nums=nums, k=k)
        print(f"boolean flag: {bool_flag}")
    except Exception as e:
        print(f"generic exception: {str(e)}")

if __name__ == "__main__":
    main()