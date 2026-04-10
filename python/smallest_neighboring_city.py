from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        INF = distanceThreshold + 1

        def dijkstra(start):
            pq = []
            pq.append((0, start))
            dists = [INF] * n
            dists[start] = 0
            adj = set()
            while pq:
                dist, node = heappop(pq)
                if dist > dists[node]:
                    continue
                for v, w in graph[node]:
                    cdist = w + dist
                    if cdist <= distanceThreshold and cdist < dists[v]:
                        dists[v] = cdist
                        heappush(pq, (cdist, v))
                        adj.add(v)
            return len(adj)

        ans = 0
        min_nc = dijkstra(0)
        for i in range(1, n):
            nc = dijkstra(i)
            if nc <= min_nc:
                min_nc = nc
                ans = i
        return ans


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
n = 5
edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
distanceThreshold = 2
ans = Solution().findTheCity(n, edges, distanceThreshold)
print(ans)
