from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # do a bfs
        n = len(graph)
        colors = [-1 for _ in range(n)]
        queue = deque()
        for i in range(n):
            if colors[i] != -1:
                continue
            colors[i] = 0
            queue.append(i)
            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if colors[adj] == -1:
                        colors[adj] = 1 - colors[node]
                        queue.append(adj)
                    elif colors[adj] == colors[node]:
                        return False
        return True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(Solution().isBipartite(graph))
