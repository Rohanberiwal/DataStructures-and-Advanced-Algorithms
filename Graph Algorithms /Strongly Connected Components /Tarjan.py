def tarjan(graph):
    def dfs(node):
        nonlocal index
        index += 1
        low[node] = index
        stack.append(node)
        on_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in low:
                dfs(neighbor)
                low[node] = min(low[node], low[neighbor])
            elif neighbor in on_stack:
                low[node] = min(low[node], low[neighbor])

        if low[node] == index:
            scc = []
            while True:
                top = stack.pop()
                on_stack.remove(top)
                scc.append(top)
                if top == node:
                    break
            strongly_connected_components.append(scc)

    index = 0
    low = {}
    stack = []
    on_stack = set()
    strongly_connected_components = []

    for node in graph:
        if node not in low:
            dfs(node)

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

print(tarjan(graph))
