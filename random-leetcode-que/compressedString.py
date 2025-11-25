def main():
    try:
        inputStr = "a3b5c2a2"
        outputStr = solveCompression(string=inputStr)
        print(f"output string: {outputStr}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def solveCompression(string):
    if string is None:
        raise Exception(f"none type of string")
    if string == "":
        return ""
    
    finalStr = ""

    for i in range(0, len(string), 2):
        char = string[i]
        count = int(string[i+1])
        while count > 0:
            finalStr += char
            count -= 1

    return finalStr

if __name__ == "__main__":
    main()