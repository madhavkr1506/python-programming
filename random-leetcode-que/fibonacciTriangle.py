def main():
    try:
        limit = 20
        # printFibonacci(limit = limit)
        printFibonacciTriangle(limit = limit)
    except Exception as e:
        print(f"Problem: {str(e)}")

def printFibonacci(limit):
    if limit == 0:
        print("0")
    a = 0
    b = 1
    print(f"{a}\n{b}")
    itr = 0
    while itr != limit:
        nextVal = a + b
        print(nextVal)
        a = b
        b = nextVal
        itr += 1

def printFibonacciTriangle(limit):
    if limit is None:
        raise Exception(f"none type limit")
    
    if limit == 0:
        print(f"0")

    for i in range(1, limit + 1, 1):
        a = 0
        b = 1

        print(f"{b}\t")
        for j in range(1, i):
            c = a + b
            print(f"{c}\t")
            a = b
            b = c
        print("\n")

if __name__ == "__main__":
    main()