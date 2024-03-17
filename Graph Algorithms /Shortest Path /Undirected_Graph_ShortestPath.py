from collections import defaultdict, deque

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path + [node]
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [node]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
end_node = 'F'
path = shortest_path(graph, start_node, end_node)
if path:
    print("Shortest path from", start_node, "to", end_node + ":", path)
else:
    print("No path found from", start_nodre, "to", end_node)
