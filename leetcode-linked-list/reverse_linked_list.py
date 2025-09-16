def main():
    try:
        head = node(1)
        head.next = node(2)
        head.next.next = node(3)
        head.next.next.next = node(4)
        head.next.next.next.next = node(5)

        result = utility_function(head=head)
        while(result != None):
            print(result.value, end="\t")
            result = result.next


    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        prev = None
        curr = head
        next_ = None
        while(curr != None):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev

    except Exception as e:
        raise e

class node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


if __name__ == "__main__":
    main()