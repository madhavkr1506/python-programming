class ListException(Exception):
    def __init__(self, message):
        super().__init__(message)

class EmptyListException(ListException):
    pass

def check(nums:list[int])->bool:
    try:
        n1 = len(nums)
        if n1 == 0:
            raise EmptyListException(f"list of length zero")
        
        # nums is sorted and rotated

        point = 0
        for i, num in enumerate(nums):
            if i > 0:
                if num >= nums[i-1]:
                    continue
                else:
                    point = i
                    break

        rotated_by = (n1 - point) % n1
        if rotated_by == 0:
            return True
        for i in range(rotated_by):
            last = nums[-1]
            nums.pop()
            nums = [last] + nums

        for i in range(n1):
            if i > 0:
                if nums[i] - nums[i - 1] < 0:
                    return False
        return True

    except Exception as err:
        if isinstance(err, EmptyListException):
            raise err
        raise err

def main():
    try:
        nums = [5,5,6,6,6,9,1,2]
        found_flag = check(nums=nums)
        print(f"found flag: {found_flag}")
    except Exception as err:
        if isinstance(err, EmptyListException):
            print(f"empty list exception: {str(err)}")
        print(f"generic exception: {str(err)}")

if __name__ == "__main__":
    main()