def main():
    try:
        flag = utility_function()
        print(f"Flag: {flag}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        numCourses = 2
        prerequisites = [[1,0]]
        adjList = {}
        visited = [0] * numCourses
        for i in range(len(prerequisites)):
            adjList.setdefault(prerequisites[i][1], []).append(prerequisites[i][0])
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(adjList, visited, i):
                    return False
        return True
    except Exception as e:
        raise e
    
def dfs(adjList, visited, i):
    try:
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        
        visited[i] = 1
        for key, value in adjList.items():
            if key == i:
                for k in range(len(value)):
                    if not dfs(adjList, visited, value[k]):
                        return False
        visited[i] = 2
        return True
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()