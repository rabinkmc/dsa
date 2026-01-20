from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u_node, v_node):
        u = self.find(u_node)
        v = self.find(v_node)
        if u == v:
            return False
        if self.rank[u] > self.rank[v]:
            self.parent[v] = u
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = v
        else:
            self.parent[v] = u
            self.rank[u] += 1
        return True

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if n <= k:
            return 0
        edges.sort(key= lambda x: x[2])
        dsu = DSU(n)
        count = n
        for u, v, w in edges:
            if dsu.union(u, v):
                count -= 1
                if count == k:
                    return w
        return -1

n = 5
edges = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]]
k = 2
ans = Solution().minCost(n, edges, k)
print(ans)
