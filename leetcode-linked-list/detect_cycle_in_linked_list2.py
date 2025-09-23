def main():
    try:
        head = node(3)
        head.next = node(2)
        head.next.next = node(0)
        head.next.next.next = node(-4)
        head.next.next.next = head.next

        final = utility_function(head)
        if final is not None:
            print(f"Final: {final}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                pos = 0
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                    pos += 1
                return pos
        return None
            
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()