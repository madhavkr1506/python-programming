from typing import List


def main():
    try:
        points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
        count = countTrapezoids(points=points)
        print(f"count: {count}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def countTrapezoids(points: List[List[int]]) -> int: # TC: O(n) and SC: O(n)
    try:
        mod = 10 ** 9 + 7

        mem = {}
        for item in points:
            y = item[1]
            mem[y] = mem.get(y, 0) + 1

        print(mem)

        answer = 0
        prevPairs = 0

        for _, val in mem.items():
            if val < 2:
                continue
            possPairs = int (val * (val - 1)) // 2

            answer = (answer + possPairs * prevPairs) % mod

            prevPairs = (prevPairs + possPairs) % mod


        return int(answer)
    except Exception as e:
        raise Exception(str(e))

if __name__ == "__main__":
    main()