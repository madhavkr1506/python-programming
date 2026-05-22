

class ListException(Exception):
    def __init__(self, message:str):
        super().__init__(message)

class EmptyListException(ListException):
    pass

def search(nums:list[int], target:int)->int:
    try:
        if len(nums) == 0:
            raise EmptyListException(f"list length is zero")
        target_index = -1
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                target_index = mid
                break
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]: right = mid - 1
                else: left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]: left = mid + 1
                else: right = mid - 1
        return target_index
    except Exception as err:
        if isinstance(err, EmptyListException):
            raise err
        raise err
    

def main():
    try:
        nums = [4,5,6,7,0,1,2]
        # nums = [1]
        target = 7
        search_index = search(nums=nums, target=target)
        print(f"search: {search_index}")
    except Exception as err:
        if isinstance(err, EmptyListException):
            print(f"empty list exception: {str(err)}")
            return
        print(f"generic exception: {str(err)}")

if __name__ == "__main__":
    main()