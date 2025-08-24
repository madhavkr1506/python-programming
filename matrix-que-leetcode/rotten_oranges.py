
from queue import Queue
def main():
    try:
        minutes = rotten_function()
        print(f"Minutes: {minutes}")
    except Exception as e:
        print(f"Message: {e}")

def rotten_function():
    try:
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        rows = len(grid)
        cols = len(grid[0])
        queue = Queue()
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.put([i, j])
                if grid[i][j] == 1:
                    fresh += 1
        
        poss_x = [-1,0,1,0]
        poss_y = [0,-1,0,1]

        minutes = 0

        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                curr_pos = queue.get()
                prevx = curr_pos[0]
                prevy = curr_pos[1]

                for i in range(4):
                    newx = poss_x[i] + prevx
                    newy = poss_y[i] + prevy

                    if (newx >= rows or newx < 0 or newy >= cols or newy < 0):
                        continue
                    if grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        fresh -= 1
                        queue.put([newx, newy])
                
            if not queue.empty():
                minutes += 1

        return -1 if fresh > 0 else minutes
            
    except Exception as e:
        raise e
    
# TC => O(M.N)

if __name__ == "__main__":
    main()