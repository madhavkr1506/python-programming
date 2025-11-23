def main():
    try:
        recursion_()
    except Exception as e:
        print(f"Problem: {str(e)}")
    
grid : list[list[int]] = [[0] * 4 for _ in range(4)]
value = 0
def recursion_():
    global grid, valMark
    try:
        print(f"initial state of grid: {grid}")
        def checkBoundary(row, col, rows, cols, grid) -> bool:
            try:
                return (row>=0 and row<rows and col>=0 and col<cols and grid[row][col] == 0)
            except Exception as e:
                raise Exception(str(e))
        
        rows = len(grid)
        cols = len(grid[0])
        
        def depthFirstSearch(x_, y_, rows, cols, grid):
            global value
            try:
                marked = checkBoundary(x_, y_, rows, cols, grid)
                if not marked:
                    return
                value += 2
                if value % 3 == 1:
                    return
                grid[x_][y_] = value
                depthFirstSearch(x_ + 1, y_, rows, cols, grid)
                depthFirstSearch(x_ - 1, y_, rows, cols, grid)
                depthFirstSearch(x_, y_ + 1, rows, cols, grid)
                depthFirstSearch(x_, y_ - 1, rows, cols, grid)
            except Exception as e:
                raise Exception(str(e))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    depthFirstSearch(row, col, rows, cols, grid)
        
        print(f"final state of grid: {grid}")

    except Exception as e:
        raise Exception(str(e))
    
if __name__ == "__main__":
    main()