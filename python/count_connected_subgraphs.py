class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x != self.parent[x]:
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


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        subsets = []
        def dfs(i, curr):
            if i == n:
                total = 0
                for idx in curr:
                    total += nums[idx]
                if total % 2 == 0 and curr:
                    subsets.append(curr[:])
                return
            dfs(i+1, curr)
            dfs(i+1, curr + [i])
        dfs(0, [])

        def check(nodes):
            dsu = DSU(n)
            items = set(nodes)
            groups = len(nodes)
            for u, v in edges:
                if (u not in items) or (v not in items):
                    continue
                if dsu.union(u, v):
                    groups -= 1
            return groups == 1

        count = 0
        for subset in subsets:
            if check(subset):
                count += 1
        return count

nums = [1,0,1]
edges = [[0,1],[1,2]]
ans = Solution().evenSumSubgraphs(nums, edges)
print(ans)
        
