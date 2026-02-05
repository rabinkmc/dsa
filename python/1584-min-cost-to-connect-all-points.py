from typing import List


class UnionFind:
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
            self.parent[u_root] = v_root
        elif self.rank[v_root] < self.rank[u_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                u = points[i]
                v = points[j]
                mdist = abs(v[0] - u[0]) + abs(v[1] - u[1])
                edges.append((mdist, i, j))
                edges.append((mdist, j, i))

        edges.sort()
        V = len(points)
        uf = UnionFind(V)
        mst = []
        cost = 0
        for w, u, v in edges:
            if uf.union(u, v):
                mst.append((w, u, v))
                cost += w
            if len(mst) == V - 1:
                break
        return cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

print(Solution().minCostConnectPoints(points))
