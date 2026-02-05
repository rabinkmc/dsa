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
        if self.rank[u] == self.rank[v]:
            self.parent[v] = self.parent[u]
            self.rank[u] += 1
        elif self.rank[u] < self.rank[v]:
            self.parent[v] = self.parent[u]
        else:
            self.parent[u] = self.parent[v]
        return True


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        dsu = DSU(n)

        def issimilar(x, y):
            n = len(x)
            count = 0
            for i in range(n):
                if x[i] != y[i]:
                    count += 1
            return count == 2

        ans = n
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = strs[i]
                y = strs[j]
                if issimilar(x, y):
                    if dsu.union(i, j):
                        ans -= 1
        return ans


strs = ["tars", "rats", "arts", "star"]
strs = ["omv", "ovm"]
print(Solution().numSimilarGroups(strs))
