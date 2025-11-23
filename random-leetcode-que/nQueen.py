def main():
    try:
        Q = 4
        fillQueen(
            queens=Q
        )

    except Exception as e:
        print(f"Problem: {str(e)}")
    
def checkOpponent(row, col, board):
    try:
        rows_len = len(board)
        for i in range(rows_len):
            if board[row][i] == 'Q':
                return False
        
        for i in range(rows_len):
            if board[i][col] == 'Q':
                return False
        r, c = row, col
        while r >=0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        r, c = row, col
        while r >=0 and c < rows_len:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        return True
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def fillQueenUtil(board, col):
    try:
        rows_len = len(board)
        if col >= rows_len:
            return True
        for row in range(rows_len):
            if checkOpponent(row, col, board):
                board[row][col] = 'Q'
                if fillQueenUtil(board, col + 1):
                    return True
                board[row][col] = ''
        return False
    except Exception as e:
        raise Exception(f"{str(e)}")
        
def fillQueen(queens):
    try:
        board : list[list[str]] = [[''] * 4 for _ in range(4)]
        col : int = 0
        fillQueenUtil(board=board, col=col)
        print(f"Placed queens: {board}")
    except Exception as e:
        raise Exception(f"{str(e)}")
    
if __name__ == "__main__":
    main()