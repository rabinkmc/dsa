import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        if len(edges) == 0:
            return -1
        n = len(online)
        def dijikstra(graph):
            pq = []
            pq.append((0, 0))
            INF = float("inf")
            dist = [INF for _ in range(n)]
            dist[0] = 0
            while pq:
                cost, node = heapq.heappop(pq)
                if dist[node] < cost:
                    continue
                if node == n - 1:
                    return cost
                for w, adj in graph[node]:
                    cdist = cost + w
                    if cdist < dist[adj]:
                        dist[adj] = cdist
                        heapq.heappush(pq, (dist[adj], adj))
            return INF

        left = 0
        right = max(edges, key = lambda x: x[2])[2]
        ans = -1
        while left <= right:
            m = left + (right - left) // 2
            graph = [[] for _ in range(n)]
            for u, v, c in edges:
                if c >= m and online[u] and online[v]:
                    graph[u].append((c, v))
            dist = dijikstra(graph)
            if dist <= k:
                ans = m
                left = m + 1
            else:
                right = m - 1
        return ans


edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]]
online = [True,True,True,False,True]
k = 12
ans = Solution().findMaxPathScore(edges, online, k)
print(ans)
