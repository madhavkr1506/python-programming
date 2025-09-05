from queue import Queue

def main():
    try:
        root = node(3)
        root.left = node(9)
        root.right = node(20)
        root.left.left = None
        root.left.right = None
        root.right.left = node(15)
        root.right.right = node(7)
        final_list = utility_function(root)
        print(f"Final list: {final_list}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function(root):
    try:
        # direction l to r => true or direction r to l => false
        direction = True
        queue = Queue()
        queue.put(root)
        final_list = []
        while not queue.empty():
            temp = []
            size_ = queue.qsize()
            for _ in range(size_):
                curr = queue.get()
                temp.append(curr.val)
                if curr.left is not None:
                    queue.put(curr.left)
                if curr.right is not None:
                    queue.put(curr.right)
                if curr.left == None and curr.right is None:
                    continue
            if direction == True:
                final_list.append(temp)
                direction = False
            elif direction == False:
                final_list.append(list(reversed(temp)))
                direction = True
            
        return final_list
    except Exception as e:
        raise e

class node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right = right 

if __name__ == "__main__":
    main()