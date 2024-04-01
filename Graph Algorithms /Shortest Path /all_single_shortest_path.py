INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example graph represented as an adjacency matrix
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

result = floyd_warshall(graph)
for row in result:
    print(row)
