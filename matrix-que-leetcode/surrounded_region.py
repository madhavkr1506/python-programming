from queue import Queue

def main():
    try:
        grid = surrounded_function()
        print(f"Grid:\n", grid)
    except Exception as e:
        print(f"Message: {e}")

def surrounded_function():
    try:
        grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        rows = len(grid)
        cols = len(grid[0])

        queue = Queue()
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and (grid[i][j] == "O"):
                    grid[i][j] = "E"
                    queue.put([i, j])

        poss_x = [-1,0,1,0]
        poss_y = [0,-1,0,1]

        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                curr_idx = queue.get()
                prevx = curr_idx[0]
                prevy = curr_idx[1]

                for i in range(4):
                    newx = prevx + poss_x[i]
                    newy = prevy + poss_y[i]

                    if not (newx < 0 or newx >= rows or newy < 0 or newy >= cols):
                        if grid[newx][newy] == "O":
                            grid[newx][newy] = "E"
                            queue.put([newx, newy])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "E":
                    grid[i][j] = "O"
        
        return grid
                     
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    main()