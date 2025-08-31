def main():
    try:
        utility_function()
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

        rows = len(grid)
        cols = len(grid[0])
        count1 = 0
        poss_x = [-1,0,1,0]
        poss_y = [0,1,0,-1]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    

        
        print(count1)

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()