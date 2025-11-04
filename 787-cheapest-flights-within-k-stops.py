from typing import List
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        pq = [(0, src)]
        parent = list(range(n))

        graph = defaultdict(list)
        for u, v, w in graph:
            graph[u].append((v, w))
        while pq:
            cost, node = heappop(pq)
            if dist[node] < cost:
                continue
            for adj, w in graph[node]:
                cdist = w + dist[node]
                if cdist < dist[adj]:
                    dist[adj] = cdist
                    parent[adj] = node
                    heappush(pq, (cdist, adj))
        path = []
        dest = dst
        while parent[dest] != dest:
            dest = parent[dest]
            path = [dest] + path

        if len(path) > k + 1:
            return -1
        ans = 0
        for station in path:
            ans += flights[station][2]

        return ans


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src, dst, k = 0, 3, 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))
