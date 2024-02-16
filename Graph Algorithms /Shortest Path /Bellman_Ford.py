from collections import defaultdict

def bellman_ford(graph, start):
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    # The distance from the start node to itself is 0
    distances[start] = 0

    # Relax edges repeatedly to find shortest paths
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances

def shortest_path_sum(graph, start, end):
    # Run Bellman-Ford algorithm to find shortest paths from start node
    shortest_distances = bellman_ford(graph, start)
    # Return the shortest path sum from start to end node
    return shortest_distances[end]

# Example usage:
graph = {
    'A': {'B': 1, 'C': -4},
    'B': {'C': 2, 'D': 5},
    'C': {'B': -2, 'D': 1},
    'D': {'B': -5, 'C': -1}
}

start_node = 'A'
end_node = 'D'

try:
    shortest_sum = shortest_path_sum(graph, start_node, end_node)
    print("Shortest path sum from", start_node, "to", end_node, "is:", shortest_sum)
except ValueError as e:
    print(e)
