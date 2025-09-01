from queue import Queue
def main():
    try:
        topoList = utility_function()
        print(f"Order: {topoList}")
    except Exception as e:
        print(f"Message: {e}")

def utility_function():
    try:
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]

        inorder = [0] * numCourses
        adjList_ ={}
        for edge in prerequisites:
            dest, src = edge
            adjList_.setdefault(src, []).append(dest)
            inorder[dest] += 1

        queue = Queue()
        for i in range(len(inorder)):
            if inorder[i] == 0:
                queue.put(i)
        topoList = []
        while not queue.empty():
            curr = queue.get()
            topoList.append(curr)
            for nei in adjList_.get(curr, []):
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    queue.put(nei)

        return topoList
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()