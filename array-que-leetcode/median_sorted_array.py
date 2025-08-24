def main():
    try:
        median = array_function()
        print(f"Median:\t", median)
    except Exception as e:
        print(f"Message: {e}")

def array_function() -> int:
    try:
        num1 = [1, 3]
        num2 = [2]
        mid = -1
        # common practice
        num1.extend(num2)
        num1 = sorted(num1)
        if len(num1) % 2 == 1:
            mid = len(num1) // 2
        if len(num1) % 2 == 0:
            mid1 = (len(num1) // 2) - 1
            mid2 = (len(num1) // 2) + 1
            mid = (mid1 + mid2) // 2
        return num1[mid]
        
    except Exception as e:
        raise e
    
# TC => comman practice => O((M + N) log (M + N))
    
if __name__ == "__main__":
    main()