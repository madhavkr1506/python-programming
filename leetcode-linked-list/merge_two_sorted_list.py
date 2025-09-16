def main():
    try:
        head1 = node(1)
        head1.next = node(2)
        head1.next.next = node(4)

        head2 = node(1)
        head2.next = node(3)
        head2.next.next = node(4)

        dummy = utility_function(head1=head1, head2=head2)
        while(dummy != None):
            print(dummy.value, end="\t")
            dummy = dummy.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head1, head2):
    try:
        curr1 = head1
        curr2 = head2
        dummy_head = node(-1)
        dummy = dummy_head

        while(curr1 != None and curr2 != None):
            value1 = curr1.value
            value2 = curr2.value
            if value1 > value2:
                dummy.next = curr2
                dummy = dummy.next
                curr2 = curr2.next
            else:
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next
        
        while (curr1 != None):
            dummy.next = curr1
            curr1 = curr1.next
            dummy = dummy.next
        while (curr2 != None):
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next
                
        return dummy_head.next
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value = 0, next = None):
        self.value = value 
        self.next = next

if __name__ == "__main__":
    main()