def main():
    try:
        head = node(1)
        head.next = node(1)
        head.next.next = node(2)
        head.next.next.next = node(3)
        head.next.next.next.next = node(3)

        result = utility_function(head=head)
        while(result != None):
            print(result.value, end="\t")
            result = result.next
    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        curr = head
        while(curr != None and curr.next != None):
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()