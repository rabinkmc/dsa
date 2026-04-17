from typing import List
from collections import defaultdict, Counter


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
            return
        if self.rank[u] > self.rank[v]:
            self.parent[v] = self.parent[u]
        elif self.rank[u] < self.rank[v]:
            self.parent[u] = self.parent[v]
        else:
            self.parent[v] = self.parent[u]
            self.rank[u] += 1


class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)
        dsu = DSU(n)
        for a, b in allowedSwaps:
            dsu.union(a, b)
        groups = defaultdict(list)
        for i in range(n):
            pi = dsu.find(i)
            groups[pi].append(i)

        ans = 0
        for pi in groups:
            indices = groups[pi]
            source_counter = Counter(source[i] for i in indices)
            target_counter = Counter(target[i] for i in indices)
            matches = 0
            for val in source_counter:
                if val in target_counter:
                    matches = matches + min(source_counter[val], target_counter[val])
            ans = ans + (len(indices) - matches)
        return ans


source = [1, 2, 3, 4]
target = [2, 1, 4, 5]
allowedSwaps = [[0, 1], [2, 3]]

source = [1, 2, 3, 4]
target = [1, 3, 2, 4]
allowedSwaps = []

source = [1, 5, 5]
target = [5, 1, 1]
allowedSwaps = [[0, 1]]
ans = Solution().minimumHammingDistance(source, target, allowedSwaps)
print(ans)
