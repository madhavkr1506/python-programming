def main():
    try:
        events = [[1,5,3],[1,5,1],[6,6,5]]

        # result = solution(events)
        result = optimized(events=events)
        print(f"result: {result}")
    except Exception as e:
        print(f"Problem: {str(e)}")

def solution(events) -> int: # TC: O(n**2)
    try:
        n = len(events)

        max_val = 0

        events.sort()
        for s, e, v in events:
            max_val = max(max_val, v)

        for i in range (n):
            s1, e1, v1 = events[i]
            for j in range (i+1, n):
                s2, e2, v2 = events[j]
                if s2 > e1:
                    max_val = max(max_val, v1 + v2)
        return max_val

    except Exception as e:
        raise Exception(str(e))


def optimized(events): # TC: O(n log n)
    try:
        n = len(events)

        events.sort()
        import bisect

        starts = [s for s, v, e in events]

        suffix_mx = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            suffix_mx[i] = max(suffix_mx[i+1], events[i][2])

        max_val = 0

        for i in range(n):
            s, e, v = events[i]
            max_val = max(max_val, v)
            j = bisect.bisect_left(starts, e + 1)
            if j < n:
                max_val = max(max_val, v + suffix_mx[j])

        return max_val

    except Exception as e:
        raise Exception(str(e))


if __name__ == "__main__":
    main()