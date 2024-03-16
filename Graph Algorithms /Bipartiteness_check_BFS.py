from collections import deque

def is_bipartite(graph):
    if not graph:
        return True
    
    start_node = next(iter(graph))
    color = {}
    queue = deque([start_node])
    color[start_node] = 0

    while queue:
        current_node = queue.popleft()
        current_color = color[current_node]
        next_color = 1 - current_color
        
        for neighbor in graph[current_node]:
            if neighbor not in color:
                color[neighbor] = next_color
                queue.append(neighbor)
            elif color[neighbor] != next_color:
                return False
                
    return True

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(is_bipartite(graph))
