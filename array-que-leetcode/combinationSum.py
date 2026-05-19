class MissingCandidatesException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class MissingTargetException(Exception):
    def __init__(self, message: str):
        super().__init__(message)      

def combinationSum(candidates: list[int], target: int)->list[list[int]]:
    n1 = len(candidates)
    if n1 == 0: raise MissingCandidatesException(f"input candidates list is empty")
    if not target: raise MissingTargetException(f"input target is missing")
    result, temp = [], []
    helper(candidates=candidates, target=target, result=result, temp=temp, index=0)
    return result

def helper(candidates, target, result, temp, index):
    if index >= len(candidates):
        return
    if target < 0:
        return
    if target == 0:
        result.append(temp.copy())
        return
    current_value = candidates[index]
    if (current_value <= target): 
        temp.append(candidates[index])
        remaining = target - current_value
        helper(candidates=candidates, target=remaining, result=result, temp=temp, index=index)
        temp.pop()
    helper(candidates=candidates, target=target, result=result, temp=temp, index=index+1)

def main():
    try:
        """
        Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
        
        """
        candidates = [2,3,6,7]
        target = 7
        result = combinationSum(candidates=candidates, target=target)
        print(f"result: {result}")
    except MissingCandidatesException as mce:
        print(f"missing candidates exception: {str(mce)}")
    except MissingTargetException as mte:
        print(f"missing target exception: {str(mte)}")
    except Exception as e:
        print(f"generic exception: {str(e)}")


if __name__ == "__main__":
    main()