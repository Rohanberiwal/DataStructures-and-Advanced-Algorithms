def kosaraju(graph):
    def dfs(node, visited, stack):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        stack.append(node)

    def transpose(graph):
        transposed_graph = {node: [] for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                transposed_graph[neighbor].append(node)
        return transposed_graph

    def dfs_scc(node, visited, scc):
        visited.add(node)
        scc.append(node)
        for neighbor in transposed_graph[node]:
            if neighbor not in visited:
                dfs_scc(neighbor, visited, scc)

    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(node, visited, stack)

    transposed_graph = transpose(graph)
    visited.clear()
    strongly_connected_components = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs_scc(node, visited, scc)
            strongly_connected_components.append(scc)

    return strongly_connected_components

# Example usage:
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3, 6],
    6: [7],
    7: [8],
    8: [6, 9],
    9: [10, 11],
    10: [12],
    11: [4, 12],
    12: []
}

print(kosaraju(graph))
