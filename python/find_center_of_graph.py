from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for u, v in edges:
            graph[u] += 1
            graph[v] += 1
        max_nodes = 0
        ans = -1
        for node in graph:
            if graph[node] > max_nodes:
                max_nodes = graph[node]
                ans = node
        return ans


edges = [[1, 2], [2, 3], [4, 2]]
ans = Solution().findCenter(edges)
print(ans)
