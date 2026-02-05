"""
idea is to do a level order traversal and keep track of levels
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        for r, row in enumerate(grid):
            for c, orange in enumerate(row):
                if orange == 0:
                    continue
                elif orange == 1:
                    fresh += 1
                else:
                    rotten.append((r, c))
        minutes = 0
        h = len(grid)
        w = len(grid[0])
        while rotten and fresh > 0:
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for rr, cc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    i, j = r + rr, c + cc
                    if 0 <= i < h and 0 <= j < w:
                        if grid[i][j] == 0:
                            continue
                        if grid[i][j] == 2:
                            continue

                        grid[i][j] = 2
                        fresh -= 1
                        rotten.append((i, j))

        return -1 if fresh > 0 else minutes
