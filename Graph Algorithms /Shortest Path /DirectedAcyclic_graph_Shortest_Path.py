from collections import defaultdict, deque

def shortest_path_dag(graph, source):
    def topological_sort(graph):
        visited = set()
        order = deque()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            order.appendleft(node)

        for node in graph:
            if node not in visited:
                dfs(node)
        return order

    # Step 2: Relaxation of Nodes
    def relax(node, neighbor, distances, parents):
        new_distance = distances[node] + graph[node][neighbor]
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            parents[neighbor] = node

    # Initialize distances and parents
    distances = defaultdict(lambda: float('inf'))
    distances[source] = 0
    parents = {}

    # Perform topological sorting
    sorted_nodes = topological_sort(graph)

    # Step 3: Traverse the nodes in topological order and relax each edge
    for node in sorted_nodes:
        for neighbor in graph[node]:
            relax(node, neighbor, distances, parents)

    return distances, parents

# Example usage:
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'C': 1, 'D': 1},
    'C': {'D': 1},
    'D': {}
}
source_node = 'A'
distances, parents = shortest_path_dag(graph, source_node)
print("Shortest distances from", source_node + ":", distances)
print("Parents:", parents)
