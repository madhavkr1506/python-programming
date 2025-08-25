def main():
    try:
        list_ = traverse_function()
        print(f"List: {list_}")
    except Exception as e:
        print(f"Message: {e}")

def traverse_function():
    try:
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        rows = len(grid)
        cols = len(grid[0])
        list_ = []
        dict_ = {}
        for i in range(rows):
            for j in range(cols):
                dia_idx = i+j
                dict_.setdefault(dia_idx, []).append(grid[i][j])
        
        for key, value in dict_.items():
            if key % 2 == 0:
                list_.extend(reversed(value))
            else:
                list_.extend(value)

        return list_
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    main()