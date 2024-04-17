class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        min_cost = 0
        pq = [(0, 0)] 
        while pq:
            cost, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            min_cost += cost
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(pq, (dist, v))
        
        return min_cost
