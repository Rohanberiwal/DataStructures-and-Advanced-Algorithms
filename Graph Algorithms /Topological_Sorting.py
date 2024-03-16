def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        sorted_nodes.append(node)

    visited = set()
    sorted_nodes = []

    for node in graph:
        if node not in visited:
            dfs(node)

    return list(reversed(sorted_nodes))

# Example usage:
graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [6],
    6: []
}

print(topological_sort(graph))  # Output: [1, 3, 5, 2, 4, 6]
