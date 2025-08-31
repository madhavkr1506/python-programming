def main():
    try:
        perimeter = utility_function()
        print(f"Perimeter: {perimeter}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

        rows = len(grid)
        cols = len(grid[0])
        peri = 0
        poss_x = [1,0]
        poss_y = [0,-1]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                elif grid[row][col] == 1:
                    peri += 4
                    for k in range(2):
                        new_x = row + poss_x[k]
                        new_y = col + poss_y[k]
                        if new_x < 0 or new_x >= rows or new_y < 0 or new_y >=cols:
                            continue
                        if grid[new_x][new_y] == 1:
                            peri -= 2
        return peri

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()