def main():
    try:
        head = node(1)
        head.next = node(2)
        head.next.next = node(3)
        head.next.next.next = node(4)
        
        final = utility_function(head)
        while final:
            print(final.value, end="\t")
            final = final.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        dummynode = node(-1)
        dummynode.next = head
        prev = dummynode
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        
        return dummynode.next
    except Exception as e:
        raise e

class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()