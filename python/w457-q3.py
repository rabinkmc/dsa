from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, un, vn):
        u = self.find(un)
        v = self.find(vn)
        if u == v:
            return False
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
        return True


class Solution2:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if len(edges) == 0:
            return 0
        edges.sort(key = lambda x: -x[2])
        count = n
        dsu = DSU(n)
        for u, v, t in edges:
            if dsu.union(u, v):
                count -= 1
                if count < k:
                    return t
        return 0

class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if len(edges) == 0:
            return 0

        def dfs(graph, t):
            components = 0
            visited = [False]*n
            for i in range(n):
                if visited[i]:
                    continue
                stack = [i]
                while stack:
                    node = stack.pop()
                    for adj, t2 in graph[node]:
                        if t2 > t and not visited[adj]:
                            visited[adj] = True
                            stack.append(adj)
                components += 1
            return components

        graph = [[] for _ in range(n)]
        left, right = 0, 0

        for u, v, t in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
            right = max(right, t)

        ans = 0
        while left <= right:
            m = left + (right - left) // 2
            if dfs(graph, m) >= k:
                ans = m
                right = m - 1
            else:
                left = m + 1
        return ans




n = 3
edges = [[0, 1, 2], [1, 2, 4]]
k = 3

n = 2
edges = [[1,0, 266]]
k = 2

sol = Solution().minTime(n, edges, k)
print(sol)
