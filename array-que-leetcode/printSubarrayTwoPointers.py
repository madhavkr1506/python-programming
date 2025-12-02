def main():
    try:
        string = "abc"
        twoPointers(string=string)
    except Exception as e:
        print(f"Problem: {str(e)}")

def twoPointers(string: str) -> None:
    try:
        left = 0
        right = left+1
        while left <= right:
            print(string[left:right])
            if right == (len(string)):
                left += 1
                right = left
            if left == len(string):
                break
            right += 1
            


    except Exception as e:
        raise Exception(str(e))
    
if __name__ == "__main__":
    main()