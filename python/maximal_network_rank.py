from typing import List
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        pairs = set()
        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
            pairs.add((u, v))
        max_rank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                rank = graph[i] + graph[j]
                if (i, j) in pairs or (j, i) in pairs:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank


n = 4
roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
ans = Solution().maximalNetworkRank(n, roads)
print(ans)
