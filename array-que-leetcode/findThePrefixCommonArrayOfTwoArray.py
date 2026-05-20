
class ListException(Exception):
    def __init__(self, message : str):
        super().__init__(message)

class ListLengthException(ListException): 
    pass 
class EmptyListException(ListException): 
    pass

def findThePrefixCommonArray(nums1:list[int], nums2:list[int])->list[int]:
    try:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0 or n2 == 0: raise EmptyListException(f"either of lists are empty. nums1: {nums1} or nums2: {nums2}")
        if n1 - n2 != 0: raise ListLengthException(f"lists length are not same. len1: {n1} or len2: {n2}")
        seen = set()
        result = [0] * n1
        for i in range(n1):
            if nums1[i] in seen: 
                result[i]+=1
            if nums2[i] in seen: 
                result[i]+=1
            if nums1[i] == nums2[i]: 
                result[i]+=1
            if i>0: result[i]=result[i-1]+result[i]
            seen.add(nums1[i])
            seen.add(nums2[i])
        return result
    except EmptyListException as ele:
        raise ele
    except ListLengthException as lle:
        raise lle
    except Exception as e:
        raise Exception(f"execution failure: {str(e)}")

def main():
    try:
        nums1 = [1,3,2,4]
        nums2 = [3,1,2,4]

        result = findThePrefixCommonArray(nums1=nums1, nums2=nums2)
        print(f"nums1: {nums1}\tnums2: {nums2}")
        print(f"nums3: {result}")
    except EmptyListException as ele:
        print(f"empty list exception: {str(ele)}")
    except ListLengthException as lle:
        print(f"lenght list exception: {str(lle)}")
    except Exception as e:
        print(f"generic exception: {str(e)}")

if __name__ == "__main__":
    main()