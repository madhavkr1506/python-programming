def main():
    try:
        grid = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        color = 2
        grid = flood_function(grid, sr, sc, color)
        print(f"Grid:\n{grid}")
    except Exception as e:
        print(f"Message: {e}")

def flood_function(grid, sr, sc, color):
    try:
        rows = len(grid)
        cols = len(grid[0])
        original = grid[sr][sc]
        if original == color:
            return grid
        dfs(sr, sc, rows, cols, grid, color, original)
        
        return grid

    except Exception as e:
        raise e

def dfs(row, col, rows, cols, grid, color, original):
    try:
        if row < 0 or row >=rows or col < 0 or col >= cols:
            return
        if (grid[row][col] != original):
            return
        grid[row][col] = color
        dfs(row + 1, col, rows, cols, grid, color, original)
        dfs(row - 1, col, rows, cols, grid, color, original)
        dfs(row, col + 1, rows, cols, grid, color, original)
        dfs(row, col - 1, rows, cols, grid, color, original)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()