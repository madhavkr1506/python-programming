def main():
    try:
        root = Node(-10)
        root.left = Node(9)
        root.right = Node(20)
        root.right.left = Node(15)
        root.right.right = Node(7)

        path_sum = utility_function(root)
        print(f"path sum: {path_sum}")
    except Exception as e:
        print(f"Message: {e}")

global_max = float("-inf")

def utility_function(root) -> int:
    global global_max
    try:
        if root == None:
            return 0
        left_max = max(0, utility_function(root.left))
        print(f"left max: {left_max}")
        right_max = max(0, utility_function(root.right))
        print(f"right max: {right_max}")

        curr_path_sum = left_max + root.value + right_max
        print(f"curr path sum: {curr_path_sum}")
        global_max = max(global_max, curr_path_sum)
        print(f"global max sum: {global_max}")
        
        print(f"return: {root.value + max(left_max, right_max)}")
        return root.value + max(left_max, right_max)
    except Exception as e:
        raise e

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value 
        self.left = left
        self.right = right

if __name__ == "__main__":
    main()