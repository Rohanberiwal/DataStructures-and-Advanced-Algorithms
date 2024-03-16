from collections import defaultdict

def is_bipartite(graph):
    colors = {}
    stack = []

    for start_node in graph:
        if start_node not in colors:
            stack.append((start_node, 0))
            colors[start_node] = 0

            while stack:
                current_node, color = stack.pop()

                for neighbor in graph[current_node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - color
                        stack.append((neighbor, 1 - color))
                    elif colors[neighbor] == color:
                        return False

    return True

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(is_bipartite(graph))
