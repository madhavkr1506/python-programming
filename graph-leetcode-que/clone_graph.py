from queue import Queue
def main():
    try:
        node1 = create_graph()
        print(node1.value)
        clone_start = clone_graph(node1)
        print(clone_start.value)
        
    except Exception as e:
        print(f"Message: {e}")

class Node:
    def __init__(self, value = 0, neigh = None):
        self.value = value
        self.neigh = neigh if neigh is not None else []

def create_graph():
    try:
        
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neigh = [node2, node4]
        node2.neigh = [node1, node3]
        node3.neigh = [node2, node4]
        node4.neigh = [node1, node3]
        return node1
    
    except Exception as e:
        raise e

def clone_graph(node):
    try:
        if not node:
            return None
        cloned = {}
        def dfs(curr):
            try:
                if curr in cloned:
                    return cloned[curr]
                
                copy_node = Node(curr.value)
                cloned[curr] = copy_node

                for neigh_ in curr.neigh:
                    copy_node.neigh.append(dfs(neigh_))

                return copy_node
            except Exception as e:
                raise e
        return dfs(node)
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
