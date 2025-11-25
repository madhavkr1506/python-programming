def main():
    try:
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        solveObstacles(obstacleGrid)
    except Exception as e:
        print(f"Problem: {str(e)}")

def solveObstacles(obstacleGrid):
    try:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        ifPath = False
        count = 0

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            print("no possible path")
            return 0
        

        count = callDfs(0, 0, rows, cols, obstacleGrid)
        print(f"possible path: {count}")
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def callDfs(row, col, rows, cols, obstacleGrid):
    try:
        if not checkBoundary(row=row, col=col, rows=rows, cols=cols, obstacleGrid=obstacleGrid):
            return 0
        if row == rows - 1 and col == cols - 1:
            return 1
        down = callDfs(row + 1, col, rows, cols, obstacleGrid)
        right = callDfs(row, col + 1, rows, cols, obstacleGrid)

        return down + right
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def checkBoundary(row, col, rows, cols, obstacleGrid):
    try:
        return (row >= 0 and row < rows and col >= 0 and col < cols and obstacleGrid[row][col] != 1)
    except Exception as e:
        raise Exception(f"{str(e)}")
    
if __name__ == "__main__":
    main()