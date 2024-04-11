from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.capacity = [[0] * V for _ in range(V)]
    
    def add_edge(self, u, v, cap):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Adding reverse edge for residual graph
        self.capacity[u][v] = cap
    
    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True
        parent[s] = -1
        
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if not visited[v] and self.capacity[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
        return visited[t]
    
    def max_flow(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[parent[s]][s])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                v = parent[v]
        
        return max_flow

# Example usage:
graph = Graph(6)
graph.add_edge(0, 1, 16)
graph.add_edge(0, 2, 13)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 4)
graph.add_edge(2, 4, 14)
graph.add_edge(3, 2, 9)
graph.add_edge(3, 5, 20)
graph.add_edge(4, 3, 7)
graph.add_edge(4, 5, 4)

source = 0
sink = 5
print("Maximum flow:", graph.max_flow(source, sink))
