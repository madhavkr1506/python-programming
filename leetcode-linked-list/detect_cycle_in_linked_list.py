def main():
    try:
        head = node(1)
        head.next = node(3)
        head.next.next = node(5)
        head.next.next.next = head.next
        flag = utility_function(head=head)
        print(f"Cycle detection: {flag}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        curr = head
        fast = curr
        slow = curr
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False

    except Exception as e:
        raise e

class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()