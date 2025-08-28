from queue import Queue

def main():
    try:
        islands_count = max_islands()
        print(f"Maximum islands => {islands_count}")
    except Exception as e:
        print(f"Message: {e}")

def max_islands():
    try:
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max_islands_util(row, col, rows, cols, grid)
                    max_area = max(max_area, area)
        
        return max_area
    except Exception as e:
        raise e
    
def max_islands_util(row, col, rows, cols, grid):
    try:
        queue = Queue()

        grid[row][col] = 0

        queue.put([row, col])

        poss_x = [-1, 0, 1, 0]
        poss_y = [0, -1, 0, 1]

        area = 1
        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                curr_idx = queue.get()
                prev_x, prev_y = curr_idx
                for i in range(4):
                    new_x = prev_x + poss_x[i]
                    new_y = prev_y + poss_y[i]
                    if (new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols):
                        continue
                    if (grid[new_x][new_y] == 0):
                        continue
                    grid[new_x][new_y] = 0
                    queue.put([new_x, new_y])
                    area += 1
        return area

    except Exception as e:
        raise e
    

# TC => O(M X N)
if __name__ == "__main__":
    main()