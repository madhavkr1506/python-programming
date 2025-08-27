from queue import Queue

def main():
    try:
        conn_components = graph_function()
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
    
if __name__ == "__main__":
    main()