def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in graph.adj_list[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
