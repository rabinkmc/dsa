from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = self.parent[v_root]
        elif self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = self.parent[u_root]
        else:
            self.parent[v_root] = self.parent[u_root]
            self.rank[u_root] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        pairs = []
        for u in range(n - 1):
            for v in range(u + 1, n):
                x1, y1 = points[u]
                x2, y2 = points[v]
                dist = abs(x2 - x1) + abs(y2 - y1)
                pairs.append((dist, u, v))
        pairs.sort()
        dsu = DSU(n)
        ans = 0
        for dist, u, v in pairs:
            if dsu.union(u, v):
                ans += dist
        return ans


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
ans = Solution().minCostConnectPoints(points)
print(ans)
