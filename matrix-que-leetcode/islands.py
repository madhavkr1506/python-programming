import datetime
print(datetime.date.today().strftime("%d-%m-%Y"))


def main():
    islands()


def islands():
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    rows = len(grid2)
    cols = len(grid2[0])
    grid1 = [[0]*cols for _ in range(rows)]

    for i in range (rows):
        for j in range(cols):
            
            if grid2[i][j] == "1":
                grid1[i][j] = 1
            else:
                grid1[i][j] = 0

    print("Islands before exploration\n",grid1)

    total_islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid1[i][j] == 1:
                total_islands += 1
                dfs(grid1, i, j, rows, cols)
    
    print("Islands after exploration\n", grid1)
    print(f"Total islands: {total_islands}")


def dfs(grid:list[list], row:int, col:int, rows:int, cols:int):
    if row >= rows or row < 0 or col < 0 or col >= cols:
        return
    if grid[row][col] != 1:
        return
    grid[row][col] = 0
    dfs(grid=grid, row=row + 1, col=col, rows=rows, cols=cols) 
    dfs(grid=grid, row=row - 1, col=col, rows=rows, cols=cols) 
    dfs(grid=grid, row=row, col=col + 1, rows=rows, cols=cols) 
    dfs(grid=grid, row=row, col=col - 1, rows=rows, cols=cols) 

if __name__ == "__main__":
    main()