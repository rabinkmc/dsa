from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        queue.append((0, 0))
        visited = set((0, 0))
        dd = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
        ]
        if grid[0][0] == 1:
            return -1
        step = 1
        while queue:
            qs = len(queue)
            for _ in range(qs):
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return step
                for dr, dc in dd:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr >= n or cc < 0 or cc >= n:
                        continue
                    if (rr, cc) in visited:
                        continue
                    if grid[rr][cc] == 0:
                        queue.append((rr, cc))
                        visited.add((rr, cc))
            step += 1
        return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
grid = [[1,0,0],[1,1,0],[1,1,0]]
ans = Solution().shortestPathBinaryMatrix(grid)
print(ans)
