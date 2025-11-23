def main():
    try:
        num = 3
        backtracking(num=num)
    except Exception as e:
        print(f"Problem: {str(e)}")
    
def backtracking(num):
    try:
        current_string = ""
        # printBinary(num, current_string)


        # 2. solve using list
        path : list[str] = []
        solveUsingList(num, path)
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def printBinary(num, current_string):
    try:
        if len(current_string) == num:
            print(current_string)
            return
        printBinary(num=num, current_string=current_string + '0')
        if not current_string or current_string[-1] == '0':
            printBinary(num=num, current_string=current_string + '1')
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def solveUsingList(num, path : list[str]):
    try:
        if len(path) == num:
            print("".join(path))
            return
        path.append('0')
        solveUsingList(num=num, path=path)
        path.pop()

        if not path or path[-1] == '0':
            path.append('1')
            solveUsingList(num=num, path=path)
            path.pop()

    except Exception as e:
        raise Exception(f"{str(e)}")

if __name__ == "__main__":
    main()