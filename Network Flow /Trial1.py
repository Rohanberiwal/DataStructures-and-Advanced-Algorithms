Attempt gives 3 as the ans 
class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = {'capacity': capacity}
        self.graph[v][u] = {'capacity': 0}

    def bfs(self, parent, source, sink):
        visited = set()
        queue = Queue()
        queue.put(source)
        visited.add(source)
        parent[source] = -1

        while not queue.empty():
            u = queue.get()
            for v, values in self.graph[u].items():
                if v not in visited and values['capacity'] > 0:
                    queue.put(v)
                    visited.add(v)
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        max_flow = 0
        parent = {}
        while self.bfs(parent, source, sink):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s]['capacity'])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v]['capacity'] -= path_flow
                self.graph[v][u]['capacity'] += path_flow
                v = parent[v]
        return max_flow

def fits_inside(box1, box2):
    return all(b1 < b2 for b1, b2 in zip(box1, box2))

def construct_graph(boxes):
    graph = Graph()
    source = 's'
    sink = 't'
    num_boxes = len(boxes)

    # Add edges from source to boxes
    for i in range(num_boxes):
        graph.add_edge(source, f'b_{i}', capacity=1)
        graph.add_edge(f'b_{i}', f'b_complement_{i}', capacity=1)

    # Add edges from boxes to sink
    for i in range(num_boxes):
        graph.add_edge(f'b_complement_{i}', sink, capacity=1)

    # Add edges between boxes
    for i in range(num_boxes):
        for j in range(num_boxes):
            if fits_inside(boxes[i], boxes[j]) and i != j:
                graph.add_edge(f'b_{i}', f'b_complement_{j}', capacity=1)

    return graph

def min_visible_boxes(boxes):
    graph = construct_graph(boxes)
    max_flow = graph.ford_fulkerson('s', 't')
    min_visible = len(boxes) - max_flow // 2  # Each box has two nodes, so divide by 2
    return min_visible

# Example usage:
boxes = [
    (15, 15, 15),
    (18, 18, 18),
    (12, 12, 12),
    (16, 16, 16),
    (20, 20, 20)
]

print("Minimum number of visible boxes:", min_visible_boxes(boxes))
