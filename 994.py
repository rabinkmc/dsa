from typing import List
from collections import deque

"""
do a bfs from every fresh orange to rotten orange
and the maximum of all the bfs's is the answer
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 0 or orange == 2:
                    continue
                if orange == 1:
                    temp = self.bfs(r, c, grid)
                    if temp == -1:
                        return -1
                    ans = max(ans, temp)

        return ans

    def bfs(self, r, c, grid):
        h = len(grid)
        w = len(grid[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        queue.append((r, c, 0))

        while queue:
            r, c, minute = queue.popleft()
            if grid[r][c] == 2:
                return minute
            for dd in direction:
                dr, dc = dd
                rr = r + dr
                cc = c + dc
                if 0 <= rr < h and 0 <= cc < w:
                    if grid[rr][cc] == 0:
                        continue
                    queue.append((rr, cc, minute + 1))

        return -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# grid = [[0, 2]]
print(Solution().orangesRotting(grid))
