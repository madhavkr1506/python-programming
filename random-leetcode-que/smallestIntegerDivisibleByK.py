def main():
    try:
        k = 1
        result = findInteger(k=k)
        print(f"result: {result}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def findInteger(k):
    try:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        mod = 0
        for length in range(1, k+1):
            mod = (mod * 10 + 1) % k
            if mod == 0:
                return length
        return -1
    except Exception as e:
        raise Exception(f"{str(e)}")
    
if __name__ == "__main__":
    main()