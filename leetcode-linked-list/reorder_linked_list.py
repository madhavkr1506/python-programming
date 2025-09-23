def main():
    try:
        head = node(1)
        head.next = node(2)
        head.next.next = node(3)
        head.next.next.next = node(4)
        head.next.next.next.next = node(5)

        final = utility_function(head)
        while final is not None:
            print(final.value, end="\t")
            final = final.next
    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        prev = None
        curr = second_half
        next_ = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        return head        
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = None

if __name__ == "__main__":
    main()