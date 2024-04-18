from collections import deque

class BipartiteMatching:
    def __init__(self, graph):
        self.graph = graph
        self.matching = {}
        self.visited = {}
        self.distance = {}
        self.MAX_DIST = float('inf')

    def hopcroft_karp(self):
        matching_size = 0
        while self.bfs():
            for u in self.graph.keys():
                if u not in self.matching and self.dfs(u):
                    matching_size += 1
        return matching_size

    def bfs(self):
        queue = deque()
        for u in self.graph.keys():
            if u not in self.matching:
                self.distance[u] = 0
                queue.append(u)
            else:
                self.distance[u] = self.MAX_DIST
        self.distance[None] = self.MAX_DIST

        while queue:
            u = queue.popleft()
            if u is not None:
                for v in self.graph[u]:
                    if self.distance[self.matching.get(v)] == self.MAX_DIST:
                        self.distance[self.matching.get(v)] = self.distance[u] + 1
                        queue.append(self.matching.get(v))
        return self.distance[None] != self.MAX_DIST

    def dfs(self, u):
        if u is not None:
            for v in self.graph[u]:
                if self.distance[self.matching.get(v)] == self.distance[u] + 1 and self.dfs(self.matching.get(v)):
                    self.matching[v] = u
                    self.matching[u] = v
                    return True
            self.distance[u] = self.MAX_DIST
            return False
        return True

# Example usage:
graph = {
    'A': ['W', 'X'],
    'B': ['W', 'Y', 'Z'],
    'C': ['X', 'Z']
}
bm = BipartiteMatching(graph)
print("Size of maximum matching:", bm.hopcroft_karp())
print("Matching pairs:", bm.matching)
