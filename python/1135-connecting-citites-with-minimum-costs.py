from typing import List

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return False
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1
        return True

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key = lambda x:x[2])
        dsu = DSU(n)
        mst_edges = []
        ans = 0
        
        for u, v, w in connections:
            if dsu.union(u-1, v-1):
                mst_edges.append((u-1, v-1))
                ans += w
            if len(mst_edges) == n - 1:
                return ans

        if len(mst_edges) < n - 1:
            return -1
        return ans

n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
ans = Solution().minimumCost(n, connections)
print(ans)

