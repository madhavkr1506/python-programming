def main():
    try:
        mat = [
                [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]
            ]
        
        print(f"initial state of sudko\n")
        for row in mat:
            print(" ".join(map(str, row)))

        fillSudko(mat=mat, row=0, col=0)

        print(f"\n\nfinal state of sudko\n")
        for row in mat:
            print(" ".join(map(str, row)))
    except Exception as e:
        print(f"Problem: {str(e)}")

def isCheck(mat, row, col, num):
    try:
        for i in range(9):
            if mat[row][i] == num:
                return False
        
        for i in range(9):
            if mat[i][col] == num:
                return False
            
        nestedRowStart = row - (row % 3)
        nestedColStart = col - (col % 3)

        for i in range(3):
            for j in range(3):
                if mat[i + nestedRowStart][j + nestedColStart] == num:
                    return False
        return True
    except Exception as e:
        raise Exception(f"{str(e)}")

def fillSudko(mat, row, col):
    try:
        if row == 8 and col == 9:
            return True
        
        if col == 9:
            row += 1
            col = 0
        if mat[row][col] != 0:
            return fillSudko(mat=mat, row=row, col=col+1)
        
        for num in range(1, 10, 1):
            if isCheck(mat, row, col, num):
                mat[row][col] = num
                if fillSudko(mat=mat, row=row, col=col+1):
                    return True
                mat[row][col] = 0
        
        return False
    except Exception as e:
        raise Exception(f"{str(e)}")


if __name__ == "__main__":
    main()
