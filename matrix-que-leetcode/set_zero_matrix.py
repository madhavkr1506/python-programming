from queue import Queue
def main():
    try:
        grid = matrix_function()
        print(f"List: {grid}")
    except Exception as e:
        print(f"Message: {e}")

def matrix_function():
    try:
        grid = [[1,1,1],[1,0,1],[1,1,1]]
        rows = len(grid)
        cols = len(grid[0])

        queue = Queue()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.put([i, j])
        
        while not queue.empty():
            curr_idx = queue.get()
            row, col = curr_idx
            for i in range(cols):
                grid[row][i] = 0
                    
            for i in range(rows):
                grid[i][col] = 0
        
        return grid
    except Exception as e:
        raise e
    
# TC => O(M X N + M X N X (M + N)) => O(M X N X (M + N))
    
if __name__ == "__main__":
    main()