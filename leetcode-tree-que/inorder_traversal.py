def main():
    try:
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)

        utility_function(root)

    except Exception as e:
        print(f"Message: {e}")

def utility_function(root):
    try:
        stack = []
        if root is not None:
            curr = root
            while stack or curr:
                if curr != None:
                    stack.append(curr)
                    curr = curr.left
                else:
                    curr = stack.pop()
                    print(curr.value, end="\t")
                    curr = curr.right
    except Exception as e:
        raise e

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

if __name__ == "__main__":
    main()