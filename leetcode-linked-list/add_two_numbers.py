def main():
    try:
        head1 = node(2)
        head1.next = node(4)
        head1.next.next = node(3)

        head2 = node(5)
        head2.next = node(6)
        head2.next.next = node(4)

        final = utility_function(head1, head2)
        while final is not None:
            print(final.value, end="\t")
            final = final.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head1, head2):
    try:
        carry = 0
        curr1 = head1
        curr2 = head2
        dummy = node(-1)
        dummynode = dummy
        while curr1 is not None or curr2 is not None or carry != 0:
            total = 0
            if curr1:
                total += curr1.value
                curr1 = curr1.next
            if curr2:
                total += curr2.value
                curr2 = curr2.next
            total += carry
            digit = total % 10
            carry = total // 10
            dummynode.next = node(digit)
            dummynode = dummynode.next
        
        return dummy.next
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value=0, next=None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()