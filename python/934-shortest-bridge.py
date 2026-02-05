from typing import List
from collections import deque

"""
|1 1 1 1 1|
|1 0 0 0 1|
|1 0 1 0 1|
|1 0 0 0 1|
|1 1 1 1 1|
"""


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def get_start_nodes(start):
            stack = [start]
            visited = set()
            start_nodes = deque()
            while stack:
                r, c = stack.pop()
                grid[r][c] = 2
                start_nodes.append((r, c))
                dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dd:
                    rr, cc = r + dr, c + dc
                    if (rr, cc) in visited:
                        continue
                    if rr < 0 or rr >= m or cc < 0 or cc >= n:
                        continue
                    if grid[rr][cc] == 1:
                        stack.append((rr, cc))
                        visited.add((rr, cc))
            return start_nodes

        def start_nodes():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return get_start_nodes((i, j))
            return deque()

        queue = start_nodes()
        visited = set()
        for r, c in queue:
            visited.add((r,c))
        step = 0
        while queue:
            qs = len(queue)
            for _ in range(qs):
                r, c = queue.popleft()
                dd = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dd:
                    rr, cc = r + dr, c + dc
                    if (rr, cc) in visited:
                        continue
                    if rr < 0 or rr >= m or cc < 0 or cc >= n:
                        continue
                    if grid[rr][cc] == 1:
                        return step  
                    queue.append((rr, cc))
                    visited.add((rr,cc))
            step += 1
        return step 

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
grid = [[0,1,0],[0,0,0],[0,0,1]]
step = Solution().shortestBridge(grid)
