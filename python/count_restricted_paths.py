from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        dists = [float("inf")] * n
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u - 1].append((v - 1, w))
            graph[v - 1].append((u - 1, w))
        pq = [(0, n - 1)]
        dists[n - 1] = 0
        while pq:
            dist, node = heappop(pq)
            if dists[node] < dist:
                continue
            for adj, w in graph[node]:
                cdist = dist + w
                if cdist < dists[adj]:
                    dists[adj] = cdist
                    heappush(pq, (cdist, adj))
        ans = 0
        print(dists)
        for i in range(n - 1):
            if dists[i] > dists[i + 1]:
                ans += 1
        return ans


n = 5
edges = [[1, 2, 3], [1, 3, 3], [2, 3, 1], [1, 4, 2], [5, 2, 2], [3, 5, 1], [5, 4, 10]]
n = 7
edges = [
    [1, 3, 1],
    [4, 1, 2],
    [7, 3, 4],
    [2, 5, 3],
    [5, 6, 1],
    [6, 7, 2],
    [7, 5, 3],
    [2, 6, 4],
]
ans = Solution().countRestrictedPaths(n, edges)
print(ans)
