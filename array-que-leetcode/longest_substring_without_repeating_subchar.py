def main():
    try:
        string1 = "abcabcbb"
        val = sliding_window(string1)
        print(f"value: {val}")
        
    except Exception as e:
        print(f"Message: {e}")

def naive_approach(string1 : str) -> int:
    max_len = 0
    try:
        def check_unique(str_ : str) -> bool:
            try:
                set_ = set()
                for i in range(len(str_)):
                    if str_[i] not in set_:
                        set_.add(str_[i])
                    else:
                        return False, -1
                return True, len(set_)
            except Exception as e:
                raise Exception(f"failed to check unique chars in a string: {str(e)}")
            
        len_ = len(string1)
        for i in range(len_):
            for j in range(i+1, len_+1):
                substr = string1[i:j]
                flag, substr_len = check_unique(substr)
                if flag:
                    max_len = max(max_len, substr_len)
        
        return max_len
    except Exception as e:
        raise e
    
# Naive approach TC: O(N^3)

def sliding_window(string: str) -> int:
    try:
        start = 0
        max_len = 0
        seen = set()
        for end in range(len(string)):
            while string[end] in seen:
                seen.remove(string[start])
                start += 1 
            seen.add(string[end])
            max_len = max(max_len, end-start+1)
        return max_len
        
    except Exception as e:
        raise Exception(str(e))

# Sliding window TC: O(N)
    
if __name__ == "__main__":
    main()