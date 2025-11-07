def main():
    try:
        def create_linked_list():
            try:
                head = Node(1)
                print(f"head node value: ", head.value)
            except Exception as e:
                raise Exception(str(e))
    except Exception as e:
        print(f"Message: {e}")

class Node:
    def __init__(self, value, next_, prev_):
        self.value = value 
        self.next_ = next_
        self.prev_ = prev_