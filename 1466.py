from typing import List
from collections import defaultdict

"""
The idea is to a dfs on graph and keep track of the sign you are using 
"""


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def get_graph(n, connections):
            graph = [[] for _ in range(n)]
            for start, end in connections:
                graph[start].append((end, 1))
                graph[end].append((start, 0))
            return graph

        visited = [False] * n
        self.count = 0

        def dfs(node):
            visited[node] = True
            for next, isoriginal in graph[node]:
                if visited[next]:
                    continue
                if isoriginal:
                    self.count += 1
                dfs(next)

        graph = get_graph(n, connections)
        dfs(0)
        return self.count


n = 6
start = 0
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]


print(Solution().minReorder(n, connections))
