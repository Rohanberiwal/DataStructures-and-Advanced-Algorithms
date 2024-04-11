function BFS(graph, source, target, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(source)
    visited[source] = True
    parent[source] = -1

    while queue:
        u = queue.pop(0)
        for v in range(len(graph)):
            if visited[v] is False and graph[u][v] > 0:
                queue.append(v)
                parent[v] = u
                visited[v] = True

    return True if visited[target] else False

function edmondsKarp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
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
