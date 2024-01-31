from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        graph = defaultdict(list)
        RED, BLUE = 1, 2
        for u, v in  redEdges:
            graph[u].append((v, RED))
        for u, v in  blueEdges:
            graph[u].append((v, BLUE))

        queue = deque()
        # (node, dist, color)
        START = (0, 0, 0)
        queue.append(START)
        ans = [-1]*n
        # node and prev color
        visited = set((0, 0))
        while queue:
            node, dist, edge_color = queue.popleft()
            if ans[node] == -1:
                ans[node] = dist
            for next_node, color in graph[node]:
                if (next_node, color) not in visited and edge_color !=  color:
                    visited.add((next_node, color))
                    queue.append((next_node, dist + 1, color))
        return ans

print(Solution().shortestAlternatingPaths(n = 3, redEdges = [[0,1],[1,2]], blueEdges = []))
