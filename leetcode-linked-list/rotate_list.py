def main():
    try:
        head = node(1)
        head.next = node(2)
        head.next.next = node(3)
        head.next.next.next = node(4)
        head.next.next.next.next = node(5)

        k = 2

        final = utility_function(head, k)
        while final:
            print(final.val, end="\t")
            final = final.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head, k):
    try:
        if not head or k == 0:
            return head
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        k %= length
        curr = head
        while curr.next:
            curr = curr.next

        curr.next = head
        curr = head

        for _ in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None        

        return new_head

        
    except Exception as e:
        raise e

class node:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

if __name__ == "__main__":
    main()