
from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:

        graph = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))
    
        max_heap = [(-1, start_node)]
        max_prob = [0] * n
        max_prob[start_node] = 1
        
        while max_heap:
            curr_prob, node = heappop(max_heap)
            curr_prob = -curr_prob
            
            if node == end_node:
                return curr_prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0
