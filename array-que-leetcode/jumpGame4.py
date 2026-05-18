
from collections import defaultdict, deque
def minJumps(arr : list[int]) -> int:
    try:
        min_jumps = helper(arr=arr)
        return min_jumps
    except Exception as e:
        raise Exception(f"{minJumps.__name__}: {str(e)}")
    
def helper(arr : list[int]) -> int:
    n = len(arr)
    if n == 1:
        return 0
    
    graph = defaultdict(list)
    for i, value in enumerate(arr):
        graph[value].append(i)

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        index, jump = queue.popleft()
        if index == n - 1:
            return jump
        neighbors = []
        if index + 1 < n:
            neighbors.append(index + 1)
        if index - 1 >= 0:
            neighbors.append(index - 1)
        neighbors.extend(graph[arr[index]])

        for next_index in neighbors:
            if next_index not in visited:
                visited.add(next_index)
                queue.append((next_index, jump + 1))
        graph[arr[index]].clear()

    return -1

def main():
    try:
        arr = [100,-23,-23,404,100,23,23,23,3,404]
        min_jumps = minJumps(arr=arr)
        print(f"minimum jumps: {min_jumps}")
    except Exception as e:
        print(f"{str(e)}")

if __name__ == "__main__":
    main()