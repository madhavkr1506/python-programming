def main():
    try:
        head = node("A")
        head.next = node("B")
        head.next.next = node("C")

        head.random = head.next.next
        head.next.random = head
        head.next.next.random = None

        final = utility_function(head)

        while final:
            print(final.val, end="\t")
            final = final.next

    except Exception as e:
        print(f"Message: {e}")

def utility_function(head):
    try:
        # TC: O(N) and SC: O(N)
        # temp_dict = {}
        # curr = head
        # while curr:
        #     temp_dict[curr] = node(curr.val)
        #     curr = curr.next
        # curr = head
        # while curr:
        #     if curr.next:
        #         temp_dict[curr].next = temp_dict[curr.next]
        #     if curr.random:
        #         temp_dict[curr].random = temp_dict[curr.random]
        #     curr = curr.next
        
        # return temp_dict[head]


        # TC: O(N) and SC: O(1)

        curr = head

        while curr:
            newnode = node(curr.val)
            newnode.next = curr.next
            curr.next = newnode
            curr = newnode.next

        curr = head
        
        while curr:
            clone = curr.next
            if curr.random:
                clone.random = curr.random.next
            curr = clone.next

        curr = head
        clonenode = head.next

        while curr:
            clone = curr.next
            curr.next = clone.next
            if clone.next:
                clone.next = clone.next.next
            curr = curr.next
        
        return clonenode
    except Exception as e:
        raise e
    
class node:
    def __init__(self, val = "", next = None, random = None):
        self.val = val 
        self.next = next 
        self.random = random

if __name__ == "__main__":
    main()