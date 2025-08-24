from queue import Queue
import math

def main():
    try:
        grid = wall_function()
        print(f"Grid\n", grid)
    except Exception as e:
        print(F"Message: {e}")

def wall_function():
    try:
        grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]

        rows = len(grid)
        cols = len(grid[0])

        queue = Queue()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.put([i, j])


        poss_x = [-1,0,1,0]
        poss_y = [0,-1,0,1]
        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                curr_pair = queue.get()
                prevx = curr_pair[0]
                prevy = curr_pair[1]

                for i in range(4):
                    newx = prevx + poss_x[i]
                    newy = prevy + poss_y[i]

                    if newx >= rows or newx < 0 or newy >= cols or newy < 0 or grid[newx][newy] == -1:
                        continue
                    if grid[newx][newy] == 2147483647:
                        grid[newx][newy] = grid[prevx][prevy] + 1
                        queue.put([newx, newy])

        return grid
    except Exception as e:
        raise e
    

if __name__ == "__main__":
    main()