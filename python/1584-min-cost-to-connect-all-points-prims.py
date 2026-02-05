from typing import List
from heapq import heappop, heappush


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst_edges = []
        visited = set()
        visited.add(0)
        n = len(points)
        pq = []
        x1, y1 = points[0]
        for j in range(1, n):
            x2, y2 = points[j]
            w = abs(x2 - x1) + abs(y2 - y1)
            heappush(pq, (w, 0, j))

        cost = 0
        while pq:
            w, u, v = heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            cost += w
            mst_edges.append((w, u, v))
            for to in range(n):
                if v == to:
                    continue
                if to not in visited:
                    x1, y1 = points[v]
                    x2, y2 = points[to]
                    w = abs(x2 - x1) + abs(y2 - y1)
                    heappush(pq, (w, v, to))
        return cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

print(Solution().minCostConnectPoints(points))
