class ListException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class EmptyListException(ListException):
    pass

def getCommon(nums1 : list[int], nums2 : list[int]) -> int:
    try:
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 or n2 == 0: raise EmptyListException(f"either of list is empty or both list are empty. list1: {nums1} or list2: {nums2}")
        if n1 > n2: 
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
            return getCommon(nums1=nums2, nums2=nums1)

        for x in nums2:
            left, right = 0, n1-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums1[mid] == x:
                    return x
                if nums1[mid] > x: right = mid - 1
                else: left = mid + 1
        return -1
    except EmptyListException as ele:
        raise ele
    except Exception as e:
        raise ListException(f"failed to execute get common function: {str(e)}")
    
def main():
    try:
        nums1 = [1, 2]
        nums2 = [2, 4]
        """
        both list is sorted in non decreasing order
        """
        min_common = getCommon(nums1=nums1, nums2=nums2)
        print(f"minimum common: {min_common}")
    except ListException as le:
        print(f"empty list exception: {str(le)}")
    except Exception as e:
        print(f"general exception: {str(e)}")

if __name__ == "__main__":
    main()