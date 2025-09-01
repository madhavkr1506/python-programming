def main():
    try:
        result = utility_function()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        rows = len(heights)
        cols = len(heights[0])

        visitedPacific = [[False] * cols for _ in range(rows)]
        visitedAtlantic = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            dfs(heights, visitedPacific, i, 0, rows, cols)
            dfs(heights, visitedAtlantic, i, cols - 1, rows, cols)

        for i in range(cols):
            dfs(heights, visitedPacific, 0, i, rows, cols)
            dfs(heights, visitedAtlantic, rows - 1, i, rows, cols)

        results = []
        for i in range(rows):
            for j in range(cols):
                if visitedAtlantic[i][j] and visitedPacific[i][j]:
                    results.append([i, j])
        return results
    except Exception as e:
        raise e

def dfs(heights, visited, row, col, rows, cols):
    try:
        
        if visited[row][col]:
            return visited[row][col]
        
        current = heights[row][col]
        visited[row][col] = True

        poss_x = [-1, 0, 1, 0]
        poss_y = [0, -1, 0, 1]
        for i in range(4):
            nr = poss_x[i] + row
            nc = poss_y[i] + col
            if (0 <= nr < rows and 0 <= nc < cols) and heights[nr][nc] >= current:
                dfs(heights, visited, nr, nc, rows, cols)
        

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()