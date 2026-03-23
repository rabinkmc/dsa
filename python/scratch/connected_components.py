from typing import List


class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u_node, v_node):
        u = self.find(u_node)
        v = self.find(v_node)
        if u == v:
            return False
        ru = self.rank[u]
        rv = self.rank[v]
        if ru < rv:
            self.parent[u] = self.parent[v]
        elif ru > rv:
            self.parent[v] = self.parent[u]
        else:
            self.parent[v] = self.parent[u]
            self.rank[u] += 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        groups = n
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                groups -= 1
        return groups


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
ans = Solution().countComponents(n, edges)
print(ans)
