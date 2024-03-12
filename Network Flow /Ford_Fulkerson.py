def dfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    stack = [source]
    visited[source] = True

    while stack:
        u = stack.pop()
        for v, capacity in enumerate(graph[u]):
            if not visited[v] and capacity > 0:
                stack.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sink]


def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while dfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


# Example usage:
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source, sink = 0, 5
print("Maximum flow:", ford_fulkerson(graph, source, sink))
