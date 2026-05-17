
def canReach(arr : list[int], start: int) -> bool:
    try:
        visited = set()
        flag = helper(arr=arr, visited=visited, start=start)
        return flag
    except Exception as e:
        raise Exception(f"{canReach.__name__}: {str(e)}")
    
def helper(arr, visited, start):
    if start < 0 or start >= len(arr):
        return False
    if start in visited:
        return False
    
    visited.add(start)

    if arr[start] == 0:
        return True
    forward = helper(arr=arr, visited=visited, start=start + arr[start])
    backward = helper(arr=arr, visited=visited, start=start - arr[start])
    return forward or backward

def main():
    try:
        arr = [3,0,2,1,2]
        start = 5

        flag = canReach(arr=arr, start=start)
        print(f"flag: {flag}")
    except Exception as e:
        print(f"{str(e)}")

if __name__ == "__main__":
    main()
    