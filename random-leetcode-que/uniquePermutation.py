from typing import Counter


def main():
    try:
        string = "aab"
        findPermutation(string=string)
    except Exception as e:
        print(f"Problem: {str(e)}")
    
def findPermutation(string):
    try:
        frequency = Counter(string)
        curr = []
        def backtrack():
            try:
                if len(curr) == len(string):
                    print("".join(curr))
                    return
                
                for ch in frequency:
                    if frequency[ch] == 0:

                        continue

                    curr.append(ch)
                    frequency[ch] -= 1

                    backtrack()

                    curr.pop()
                    frequency[ch] += 1
            except Exception as e:
                raise Exception(f"{str(e)}")

        backtrack()
        
    except Exception as e:
        raise Exception(f"{str(e)}")
    
if __name__ == "__main__":
    main()