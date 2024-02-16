import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    # The distance from the start node to itself is 0
    distances[start] = 0
    # Priority queue to keep track of nodes with their current shortest distance from start
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip processing if current distance is greater than known distance
        if current_distance > distances[current_node]:
            continue

        # Iterate through neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If the new distance is shorter than the known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def shortest_path_sum(graph, start, end):
    # Run Dijkstra's algorithm to find the shortest paths from the start node
    shortest_distances = dijkstra(graph, start)
    # Return the shortest path sum from start to end node
    return shortest_distances[end]

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
end_node = 'D'

shortest_sum = shortest_path_sum(graph, start_node, end_node)
print("Shortest path sum from", start_node, "to", end_node, "is:", shortest_sum)
