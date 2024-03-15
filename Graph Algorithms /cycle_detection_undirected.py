from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, v):
                    return True
            elif parent != neighbour:
                return True

        return False

    def is_cyclic(self):
        visited = [False] * len(self.graph)

        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, -1):
                    return True
        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
