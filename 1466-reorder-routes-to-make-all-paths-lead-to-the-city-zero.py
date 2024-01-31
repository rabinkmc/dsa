from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        START = 0
        stack = [START]
        visited = [False]*n
        visited[0] = True
        ans = 0
        while stack:
            node = stack.pop()
            for next_node, is_original in graph[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                if is_original:
                    ans += 1
                stack.append(next_node)
        return ans
        
