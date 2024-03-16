from collections import defaultdict, deque

def topological_sort(graph):
    in_degree = {v: 0 for v in graph}
    
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    
    queue = deque([v for v, degree in in_degree.items() if degree == 0])
    result = []
    
    while queue:
        current_vertex = queue.popleft()
        result.append(current_vertex)
        
        for neighbor in graph[current_vertex]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(graph):
        return None
    
    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

print(topological_sort(graph))  
