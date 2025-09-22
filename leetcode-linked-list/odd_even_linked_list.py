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
        if head is None or head.next is None or head.next.next is None:
            return head
        
        odd_pointer = head
        even_pointer = head.next
        even_head = even_pointer

        while even_pointer and even_pointer.next is not None:
            odd_pointer.next = even_pointer.next
            odd_pointer = odd_pointer.next
            even_pointer.next = odd_pointer.next
            even_pointer = even_pointer.next

        odd_pointer.next = even_head

        return head
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value=0, next=None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()