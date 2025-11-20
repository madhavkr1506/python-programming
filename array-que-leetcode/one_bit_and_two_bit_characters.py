def main():
    try:
        bits = [1,0,0]
        len_ = len(bits)
        i = 0
        while i + 1 < len_:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        print(f"{i == len_ - 1}")
            
    except Exception as e:
        print(f"Problem: {str(e)}")

if __name__ == "__main__":
    main()