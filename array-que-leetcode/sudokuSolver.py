"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

"""

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]


def isvalid(row, col, opt):
    for a in range(9):
        if board[a][col] == str(opt):
            return False
    for b in range(9):
        if board[row][b] == str(opt):
            return False
    inner_grid_row = row - (row % 3)
    inner_grid_col = col - (col % 3)
    for m in range(3):
        for n in range(3):
            if board[m + inner_grid_row][n + inner_grid_col] == str(opt):
                return False
    return True

def traverse_board(board):
    empty_cells = [(row, col) for col in range(9) for row in range(9) if board[row][col] == '.']
    return empty_cells

def solve(empty_cells, index):
    if index == len(empty_cells):
        return True
    row, col = empty_cells[index]
    for opt in range(1, 10):
        allowed = isvalid(row=row, col=col, opt=opt)
        if allowed:
            board[row][col] = str(opt)
            if solve(empty_cells, index+1):
                return True
            board[row][col] = "."
    return False

empty_cells = traverse_board(board=board)
solve(empty_cells=empty_cells, index=0)
print(board)

