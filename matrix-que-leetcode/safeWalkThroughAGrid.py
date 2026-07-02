"""
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.


Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.


Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
2 <= m * n
1 <= health <= m + n
grid[i][j] is either 0 or 1.

"""

grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]
health = 3

rows, cols = len(grid), len(grid[0])
visited = [[False for _ in range(cols)] for _ in range(rows)]
besthealth = [[-1 for _ in range(cols)] for _ in range(rows)]

def helper(row, rows, col, cols, grid, health, visited, besthealth):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return False
    if visited[row][col]:
        return False
    if health > 0:
        if grid[row][col] == 1:
            health -= 1
            if health <= 0: return False
        if health <= besthealth[row][col]:
            return False
        if row == rows - 1 and col == cols - 1: return True
        visited[row][col] = True
        ans = (helper(row + 1, rows, col, cols, grid, health, visited, besthealth) or helper(row, rows, col + 1, cols, grid, health, visited, besthealth) or helper(row - 1, rows, col, cols, grid, health, visited, besthealth) or helper(row, rows, col - 1, cols, grid, health, visited, besthealth))
        besthealth[row][col] = health
        visited[row][col] = False
        return ans
    return False

flag = helper(row=0, rows=rows, col=0, cols=cols, grid=grid, health=health, visited=visited, besthealth=besthealth)
print(f"flag: {flag}")