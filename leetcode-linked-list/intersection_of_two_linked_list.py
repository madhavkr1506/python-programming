def main():
    try:
        common = node(8)
        common.next = node(4)
        common.next.next = node(5)

        head1 = node(4)
        head1.next = node(1)
        head1.next.next = common

        head2 = node(5)
        head2.next = node(6)
        head2.next.next = node(1)
        head2.next.next.next = common

        node_ = utility_function(head1=head1, head2=head2)
        print(f"Value: {node_.value}")

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head1, head2):
    try:
        p1 = head1
        p2 = head2

        while p1 != p2:
            if p1 is None:
                p1 = head2
            else:
                p1 = p1.next

            if p2 is None:
                p2 = head1
            else:
                p2 = p2.next

        return p1
        
    except Exception as e:
        raise e
    
class node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

if __name__ == "__main__":
    main()