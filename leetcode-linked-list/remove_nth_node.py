class node:
    def __init__(self, value, next = None):
        self.value = value 
        self.next = next


def main():
    try:
        head = node(1)
        head.next = node(2)
        head.next.next = node(3)
        head.next.next.next = node(4)
        head.next.next.next.next = node(5)

        n = 2
        node_ = utility_function(head, n)

        while node_ is not None:
            print(node_.value, end="\t")
            node_ = node_.next



    except Exception as e:
        print(f"Message: {e}")

def utility_function(head, n):
    try:
        dummy = node(0, head)
        fast = dummy
        slow = dummy
        i = 0
        while i < n + 1:
            fast = fast.next
            i += 1
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next      
        
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()