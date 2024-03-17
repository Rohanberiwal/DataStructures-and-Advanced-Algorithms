def floyd_warshall(graph):
    # Number of vertices
    n = len(graph)
    
    # Initialize the distances matrix with the same weights as the input graph
    distances = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
        for j in graph[i]:
            distances[i][j] = graph[i][j]
    
    # Update distances matrix by considering each vertex as an intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances

# Example usage:
graph = {
    0: {1: 3, 2: 8},
    1: {2: -4, 3: 1},
    2: {3: 7, 0: 2},
    3: {1: 2, 0: -5}
}
all_pairs_shortest_paths = floyd_warshall(graph)
print("Shortest paths between all pairs of vertices:")
for row in all_pairs_shortest_paths:
    print(row)
