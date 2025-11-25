def main():
    try:
        num1 = 70
        num2 = 15

        finalRes = findHCFWithoutRec(num1=num1, num2=num2)
        print(f"final hcf: {finalRes}")

        finalRes = findHCFWithRec(num1=num1, num2=num2)
        print(f"final hcf: {finalRes}")

    except Exception as e:
        print(f"Problem: {str(e)}")

def findHCFWithoutRec(num1, num2):
    if not num1 and not num2:
        raise Exception(f"missing values")
    if num1 == 0:
        return num2
    
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

def findHCFWithRec(num1, num2):
    if num1 == 0:
        return num2
    else:
        return findHCFWithRec(num2 % num1, num1)

if __name__ == "__main__":
    main()