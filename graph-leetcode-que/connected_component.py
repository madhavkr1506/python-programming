from queue import Queue

def main():
    try:
        # conn_components = graph_function()
        conn_components = dsu_conn_components()
        print(f"Connected components => {conn_components}")
    except Exception as e:
        print(f"Message: {e}")

def graph_function():
    try:
        edges = [[0,1],[1,2],[3,4]]
        nodes = 5

        visited = [False] * nodes
        dict_ = {}
        for node in range(nodes):
            for edge in edges:
                src, dest = edge
                if src == node:
                    dict_.setdefault(node, []).append(dest)
                if dest == node:
                    dict_.setdefault(node, []).append(src)
                
        queue = Queue()
        conn_components = 0
        for node in range(nodes):
            if not visited[node]:
                queue.put(node)
                conn_components += 1
                while not queue.empty():
                    size = queue.qsize()
                    for _ in range(size):
                        curr_node = queue.get()
                        if not visited[curr_node]:
                            visited[curr_node] = True
                            neigh_nodes = dict_[curr_node]
                            for i in range(len(neigh_nodes)):
                                if not visited[neigh_nodes[i]]:
                                    queue.put(neigh_nodes[i])
        return conn_components

    except Exception as e:
        raise e
    
# TC: (N X E)

def dsu_conn_components():
    try:
        edges = [[0,1],[1,2],[3,4]]
        nodes = 5
        parents = [node for node in range(nodes)]

        for edge in edges:
            node1, node2 = edge
            union(node1, node2, parents)
        conn_components = 1
        for node in range(len(parents)):
            if node > 0:
                if parents[node - 1] == parents[node]:
                    continue
                conn_components += 1
        return conn_components

    except Exception as e:
        raise e
    
def union(node1, node2, parents):
    try:
        parent_node1 = find(node1, parents)
        parent_node2 = find(node2, parents)
        parents[parent_node2] = parent_node1
    except Exception as e:
        raise e
    
def find(node, parents):
    try:
        if parents[node] == node:
            return node
        return find(parents[node], parents)
    except Exception as e:
        raise e


if __name__ == "__main__":
    main()