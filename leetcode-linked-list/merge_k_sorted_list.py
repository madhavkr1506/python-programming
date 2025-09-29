import heapq

def main():
    try:
        head1 = node(1)
        head1.next = node(4)
        head1.next.next = node(5)

        head2 = node(1)
        head2.next = node(3)
        head2.next.next = node(4)

        head3 = node(2)
        head3.next = node(6)

        lists = [head1, head2, head3]

        final = utility_function(lists)

        while final:
            print(final.val, end="\t")
            final = final.next
    except Exception as e:
        print(f"Message: {e}")

def utility_function(lists):
    try:
        if not lists:
            return None
        
        queue = []
        for head in lists:
            if head:
                heapq.heappush(queue, (head.val, id(head), head))

        dummy = node(-1)
        dummynode = dummy

        while queue:
            val, _, curr = heapq.heappop(queue)
            dummy.next = curr
            dummy = dummy.next
            if curr.next:
                heapq.heappush(queue, (curr.next.val, id(curr.next), curr.next))

        return dummynode.next
    except Exception as e:
        raise e
    
class node:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

if __name__ == "__main__":
    main()