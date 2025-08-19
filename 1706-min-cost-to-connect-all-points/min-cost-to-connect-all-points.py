class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        min_dist = [float('inf')] * n
        min_dist[0] = 0 

        in_mst = [False] * n

        heap = [(0, 0)]  
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            in_mst[u] = True
            total_cost += cost

            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost
