function BFS (graph, source, target, level):
    for each vertex u in graph:
        level[u] = -1
    queue = empty queue
    enqueue source into queue
    level[source] = 0
    while queue is not empty:
        current = dequeue from queue
        for each edge (current, next) in graph:
            if level[next] < 0 and capacity[current][next] > 0:
                level[next] = level[current] + 1
                enqueue next into queue
    return level[target] >= 0

function DFS (graph, source, target, level, flow):
    if source == target:
        return flow
    for each edge (source, next) in graph:
        if level[next] == level[source] + 1 and capacity[source][next] > 0:
            new_flow = DFS(graph, next, target, level, min(flow, capacity[source][next]))
            if new_flow > 0:
                capacity[source][next] -= new_flow
                capacity[next][source] += new_flow
                return new_flow
    return 0

function DinicMaxFlow (graph, source, target):
    max_flow = 0
    while BFS(graph, source, target, level):
        while flow = DFS(graph, source, target, level, INFINITY):
            max_flow += flow
    return max_flow
