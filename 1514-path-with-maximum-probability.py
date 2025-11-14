from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:

        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            w = succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [0.0] * n
        dist[start_node] = 1.0

        pq = []
        heappush(pq, (-1.0, start_node))
        while pq:
            cdist, node = heappop(pq)
            for adj, w in graph[node]:
                newdist = -cdist * w
                if newdist > dist[adj]:
                    dist[adj] = newdist
                    heappush(pq, (-newdist, adj))
        return dist[end_node]


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2
ans = Solution().maxProbability(n, edges, succProb, start, end)
print(ans)
