from collections import deque

def lexBFS(graph):
    n = len(graph)
    visited = [False] * n
    labels = [-1] * n
    ordering = []

    for start in range(n):
        if not visited[start]:
            queue = deque([start])
            while queue:
                u = queue.popleft()
                if not visited[u]:
                    visited[u] = True
                    ordering.append(u)
                    neighbors = sorted(graph[u])
                    for v in neighbors:
                        if not visited[v]:
                            queue.append(v)
    
    # Assign labels based on the order of vertices in the ordering
    for i, vertex in enumerate(ordering):
        labels[vertex] = i

    return labels

# Example undirected graph represented as an adjacency list
graph = {
    0: [1, 4],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 3]
}

lex_order = lexBFS(graph)
print("Lexicographic BFS ordering:", lex_order)
