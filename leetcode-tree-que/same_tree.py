def main():
    try:
        node1_1 = Node(1)
        node2_1 = Node(2)
        node3_1 = Node(3)
        node4_1 = Node(4)

        root_1 = node1_1
        root_1.left = node2_1
        root_1.right = node3_1

        node2_1.left = node4_1

        node1_2 = Node(1)
        node2_2 = Node(2)
        node3_2 = Node(3)
        node4_2 = Node(5)

        root_2 = node1_2
        root_2.left = node2_2
        root_2.right = node3_2

        node2_2.left = node4_2

        flag = checkSameTree(root1=root_1, root2=root_2)
        print(f"flag: {flag}")
        
    except Exception as e:
        print(f"Problem: {str(e)}")

def checkSameTree(root1 : Node, root2 : Node) -> bool:
    try:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        if root1.value != root2.value:
            return False
        
        return checkSameTree(root1.left, root2.left) and checkSameTree(root1.right, root2.right)
        
    except Exception as e:
        raise Exception(f"checkSameTree failure: {str(e)}")

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value 
        self.left = left
        self.right = right
    
if __name__ == "__main__":
    main()