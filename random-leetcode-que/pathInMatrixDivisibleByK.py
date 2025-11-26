def main():
    try:
        mat = [[5,2,4],[3,0,5],[0,7,2]]
        k = 3
        numberOfPaths(mat=mat, k=k)
    except Exception as e:
        print(f"Problem: {str(e)}")

def numberOfPaths(mat, k):
    MOD = 10**9 + 7
    if not mat:
        raise Exception(f"none type matrix")
    if k == 0:
        raise Exception(f"zero division")
    from functools import cache
    @cache
    def findPathCountUtil(row, col, currSum):
        if not (row >= 0 and row < rows and col >= 0 and col < cols):
            return 0
        currSum += mat[row][col]

        if row == rows - 1 and col == cols - 1:
            if currSum % k == 0:
                return 1

        downPath = findPathCountUtil(row+1, col, currSum=currSum)
        rightPath = findPathCountUtil(row, col+1, currSum=currSum)

        return (downPath + rightPath) % MOD
    
    rows = len(mat)
    cols = len(mat[0])

    pathCount = findPathCountUtil(row=0, col=0, currSum=0)
    findPathCountUtil.cache_clear()
    
    print(f"found path count: {pathCount}")

if __name__ == "__main__":
    main()