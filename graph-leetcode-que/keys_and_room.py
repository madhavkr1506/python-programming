def main():
    try:
        flag = utility_function()
        print(f"Flag: {flag}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        rooms = [[1,3],[3,0,1],[2],[0]]
        visited = [0] * len(rooms)
        dfs(rooms, visited, 0)
                
        return all(visited)

    except Exception as e:
        raise e
    
def dfs(rooms, visited, i):
    try:
        if visited[i] == 1:
            return
        visited[i] = 1
        nei = rooms[i]
        for k in nei:
            dfs(rooms, visited, k)

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()