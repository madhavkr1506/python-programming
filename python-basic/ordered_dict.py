from collections import OrderedDict

def main():
    try:
        sequence = [1, 2, 3, 2, 4]
        capacity = 3
        utility_function(sequence=sequence, capacity=capacity)
    except Exception as e:
        print(f"Message: {e}")

def utility_function(capacity, sequence):
    try:
        cache = OrderedDict()

        def get(key) -> int:
            if not key in cache:
                return -1
            value = cache.pop(key)
            cache[key] = value
            return value
        
        def put(key, value) -> None:
            if key in cache:
                cache.pop(key)

            elif len(cache) == capacity:
                cache.popitem(last=False)

            cache[key] = value

        def show():
            print(list(cache.keys()))

        for item in sequence:
            put(item, item)
            show()
        
        print(f"final cache: {list(cache.keys())}")

    except Exception as e:
        raise e

if __name__ == "__main__":
    main()


# TC => get O(1) or put O(1)
# SC => O(n)