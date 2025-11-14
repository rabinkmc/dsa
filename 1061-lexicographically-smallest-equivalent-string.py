class DSU:
    def __init__(self):
        self.parent = list(range(26))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u_node, v_node):
        u = self.find(u_node)
        v = self.find(v_node)
        if u == v:
            return
        if u < v:
            self.parent[v] = self.parent[u]
        else:
            self.parent[u] = self.parent[v]


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()
        for c1, c2 in zip(s1, s2):

            dsu.union(ord(c1) - ord("a"), ord(c2) - ord("a"))
        ans = []
        for ch in baseStr:
            replace = dsu.find(ord(ch) - ord("a"))
            ans.append(chr(ord("a") + replace))
        return "".join(ans)


s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
ans = Solution().smallestEquivalentString(s1, s2, baseStr)
print(ans)
