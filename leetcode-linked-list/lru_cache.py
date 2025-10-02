def main():
    try:
        operations = ["LRUCache","put","put","get","put","get","put","get","get","get"]
        values = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

        output = utility_function(operations, values)
        print(output)

    except Exception as e:
        print(f"Message: {e}")

def utility_function(operations, values):
    try:
        object_ = None
        result = []
        for op, val in zip(operations, values):
            if op == "LRUCache":
                object_ = LRUCache(val[0])
                result.append(None)
            elif op == "put":
                object_.put(val[0], val[1])
                result.append(None)

            elif op == "get":
                res = object_.get(val[0])
                result.append(res)
        return result
        
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value = 0, key = 0, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = node(0, 0)
        self.tail = node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node_ = self.cache[key]
        self._move_to_end(node_)
        return node_.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node_ = self.cache[key]
            node_.value = value
            self._move_to_end(node_)
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            new_node = node(key, value)
            self.cache[key] = new_node
            self._add(new_node)

    def _add(self, node_):
        node_.prev = self.tail.prev
        node_.next = self.tail
        self.tail.prev.next = node_
        self.tail.prev = node_


    def _remove(self, node_):
        prev_node = node_.prev
        next_node = node_.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_end(self, node_):
        self._remove(node_)
        self._add(node_)

if __name__ == "__main__":
    main()