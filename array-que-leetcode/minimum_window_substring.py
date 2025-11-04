from collections import Counter
def main():
    try:
        s = "ADOBECODEBANC"
        t = "ABC"
        final_substr = sliding_window(s, t)
        print(f"Final substring: {final_substr}")
    except Exception as e:
        print(f"Message: {str(e)}")

def sliding_window(str1 : str, str2 : str):
    try:
        if not str1 or not str2:
            return ""
        target = Counter(str2)
        need = len(target)
        have = 0

        window = {}
        left = 0
        res, res_len = [-1, -1], float("inf")

        for right, ch in enumerate(str1):
            window[ch] = window.get(ch, 0) + 1

            if ch in target and window[ch] == target[ch]:
                have += 1
            
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[str1[left]] -= 1
                if str1[left] in target and window[str1[left]] < target[str1[left]]:
                    have -= 1
                left += 1
        left, right = res
        return str1[left:right+1] if res_len != float("inf") else ""

    except Exception as e:
        raise Exception(f"problem: {str(e)}")


if __name__ == "__main__":
    main()