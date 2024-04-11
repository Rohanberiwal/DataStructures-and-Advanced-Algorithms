function BFS(graph, source, target, parent, capacity, scaling_factor):
    visited = [False] * len(graph)
    queue = []
    queue.append(source)
    visited[source] = True
    parent[source] = -1

    while queue:
        u = queue.pop(0)
        for v in range(len(graph)):
            if visited[v] is False and capacity[u][v] >= scaling_factor:
                queue.append(v)
                parent[v] = u
                visited[v] = True

    return True if visited[target] else False

function capacityScaling(graph, source, sink):
    max_capacity = max(max(row) for row in graph)
    scaling_factor = 1 << (max_capacity.bit_length() - 1)
    max_flow = 0

    while scaling_factor > 0:
        parent = [-1] * len(graph)
        while BFS(graph, source, sink, parent, capacity, scaling_factor):
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

        scaling_factor >>= 1

    return max_flow
