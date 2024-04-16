import networkx as nx

# Create a bipartite graph
G = nx.Graph()

# Add nodes to the graph. Nodes in set A are labeled as 'a1', 'a2', ..., and nodes in set B are labeled as 'b1', 'b2', ...
A = ['a1', 'a2', 'a3']
B = ['b1', 'b2', 'b3', 'b4']

# Add nodes from both sets
G.add_nodes_from(A, bipartite=0)
G.add_nodes_from(B, bipartite=1)

# Add edges between the nodes
edges = [('a1', 'b1'), ('a1', 'b2'), ('a2', 'b2'), ('a2', 'b3'), ('a3', 'b3'), ('a3', 'b4')]
G.add_edges_from(edges)

# Perform bipartite matching
matching = nx.bipartite.maximum_matching(G, top_nodes=A)

# Print the matching
print("Bipartite matching:")
for a, b in matching.items():
    print(f"{a} matches with {b}")
