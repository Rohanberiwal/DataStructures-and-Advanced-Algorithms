def has_cycle(graph):
    visited = [0] * len(graph)
    
    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if visited[neighbor] == 1:
                return True
            elif visited[neighbor] == 0:
                if dfs(neighbor):
                    return True
        visited[node] = 2
        return False

    for node in range(len(graph)):
        if visited[node] == 0:
            if dfs(node):
                return True
    return False
