def main():
    try:
        head = node(1)
        head.next = node(4)
        head.next.next = node(3)
        head.next.next.next = node(2)
        head.next.next.next.next = node(5)
        head.next.next.next.next.next = node(2)

        x = 3

        final = utility_function(head, x)
        while final:
            print(final.value, end="\t")
            final = final.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head, x):
    try:
        before_value = node(-1)
        after_value = node(-1)
        current = head

        before = before_value
        after = after_value
        while current:
            if current.value < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        before.next = after_value.next
        after.next = None

        return before_value.next

    except Exception as e:
        raise e

class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()