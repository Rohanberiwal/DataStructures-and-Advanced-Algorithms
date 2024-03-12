def print_adjacency_matrix(adj_matrix):
    for row in adj_matrix:
        print(' '.join(map(str, row)))

# Example usage:
graph_adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

adj_matrix = adjacency_matrix(graph_adj_list)

print("Adjacency Matrix:")
print_adjacency_matrix(adj_matrix)
