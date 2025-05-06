from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:  # Fix: You checked u twice, fixed to check v
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = set()
        print(node, end=' ')
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()  # Fix: added () to actually call popleft
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

def main():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    print("DFS Traversal:")
    g.dfs_recursive(0)

    print("\nBFS Traversal:")
    g.bfs(0)

if __name__ == "__main__":
    main()
