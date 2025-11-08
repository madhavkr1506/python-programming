def main():
    try:
        final_living = recursive(5, 2)
        print(f"final living: {final_living + 1}")
    except Exception as e:
        print(f"Message: {str(e)}")

def recursive(n : int, k : int) -> int:
    try:
        if n == 1:
            return 0
        print(f"n value: {n}\tk value: {k}\t")
        return (recursive(n-1, k) + k) % n
        
    except Exception as e:
        raise Exception(str(e))
    
if __name__ == "__main__":
    main()