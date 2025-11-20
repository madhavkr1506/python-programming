def main():
    try:
        nums = [5,3,6,1,12]
        original = 3

        nums = set(nums)
        while original in nums:
            original *= 2
        print(f"Original: {original}")

    except Exception as e:
        print(f"Problem: {str(e)}")

if __name__ == "__main__":
    main()