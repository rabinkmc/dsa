from typing import List


class DSU:
    def __init__(self):
        self.parent = list(range(26))
        self.rank = [0] * 26

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u_node, v_node):
        u = self.find(u_node)
        v = self.find(v_node)
        if u == v:
            return
        if self.rank[u] > self.rank[v]:
            self.parent[v] = self.parent[u]
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = self.parent[v]
        else:
            self.parent[v] = self.parent[u]
            self.rank[u] += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        for eq in equations:
            if eq[1] == "!":
                continue
            xi = ord(eq[0]) - ord("a")
            yi = ord(eq[3]) - ord("a")
            dsu.union(xi, yi)

        for eq in equations:
            if eq[1] == "=":
                continue
            xi = ord(eq[0]) - ord("a")
            yi = ord(eq[3]) - ord("a")
            if dsu.find(xi) == dsu.find(yi):
                return False
        return True


equations = ["a==b", "c==d", "a==c", "a!=d"]
ans = Solution().equationsPossible(equations)
print(ans)
