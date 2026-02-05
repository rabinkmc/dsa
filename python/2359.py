from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def dfs(start):
            d = 0
            dist = [-1] * n
            while start != -1 and dist[start] == -1:
                dist[start] = d
                d += 1
                start = edges[start]
            return dist
        d1 = dfs(node1)
        d2 = dfs(node2)
        best = float("inf")
        ans = -1
        for i in range(n):
            if d1[i] != -1 and d2[i] != -1:
                curr = max(d1[i], d2[i])
                if curr < best:
                    best = curr
                    ans = i
        return ans
edges = [2,2,3,-1]
node1 = 0
node2 = 1
edges = [2, 0, 0]
node1 = 2
node2 = 0
ans = Solution().closestMeetingNode(edges, node1, node2)
print(ans)
"""

1->0<-2

"""
