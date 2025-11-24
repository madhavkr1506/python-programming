def main():
    try:
        nums = [0,1,1]

        def checkCond(nums):
            currNum = 0
            result = []
            try:
                for bit in nums:
                    currNum = buildNum(curr=currNum, nextBit=bit)
                    if currNum % 5 == 0:
                        result.append(True)
                    else:
                        result.append(False)
                print(f"result: {result}")
            except Exception as e:
                raise Exception(f"{str(e)}")
        
        checkCond(nums=nums)
            
    except Exception as e:
        print(f"Problem: {str(e)}")

def buildNum(curr, nextBit):
    try:
        return (curr * 2 + nextBit) % 5
    except Exception as e:
        print(f"Problem: {str(e)}")

if __name__ == "__main__":
    main()