def main():
    try:
        sequence = [1, 2, 3, 2, 4]
        capacity = 1

        final_res = utility_function(sequence=sequence, capacity=capacity)
        print(f"final res: {final_res}")

    except Exception as e:
        print(f"Message: {e}")

def utility_function(sequence, capacity):
    try:
        lru_cache = LRUCache(capacity=capacity)
        for item in sequence:
            lru_cache._put(item, item)

        results = []
        node = lru_cache.head.next
        while node != lru_cache.tail:
            results.append(node.key)
            node = node.next
        return results

    except Exception as e:
        raise e
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _get(self, key) -> int:
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_end(node=node)
        return node.value

    def _put(self, key, value) -> None:
        if key in self.cache:
            node =  self.cache[key]
            node.value = value
            self.cache[key] = node
            self._move_to_end(node=node)
        else:
            if self.capacity == len(self.cache):
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            node = Node(key, value)
            self.cache[key] = node
            self._add(node=node)

    def _add(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node):
        self._remove(node)
        self._add(node)

class Node:
    def __init__(self, key = 0, value = 0, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

if __name__ == "__main__":
    main()