def main():
    try:
        # def printSubarray(arr : list): # TC: Theta(N^3)
        #     try:
        #         n = len(arr)
        #         for i in range(n):
        #             for j in range(i, n):
        #                 for k in range(i, j+1):
        #                     print(arr[k], end="\t")
        #                 print("\n")
        #     except Exception as e:
        #         raise Exception(f"{str(e)}")
        # printSubarray([1,2,3,4,5,6,7])

        def printSubarray(arr : list): # TC: Theta(N^3)
            try:
                n = len(arr)
                for i in range(n):
                    for j in range(i, n):
                        print(arr[i:j+1])
                    print("\n")
            except Exception as e:
                raise Exception(f"{str(e)}")
        printSubarray([1,2,3,4,5,6,7])
    except Exception as e:
        print(f"Message: {str(e)}")

if __name__ == "__main__":
    main()