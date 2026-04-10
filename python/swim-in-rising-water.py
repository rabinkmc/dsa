from typing import List
from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        INF = 50000
        dists = [[INF] * n for _ in range(m)]
        dists[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]
        while pq:
            dist, r, c = heappop(pq)
            if (r, c) == (m - 1, n - 1):
                return dist
            if dist > dists[r][c]:
                continue
            dd = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dx, dy in dd:
                rr, cc = r + dx, c + dy
                if rr < 0 or rr >= m or cc < 0 or cc >= n:
                    continue
                cdist = max(grid[rr][cc], dist)
                if max(grid[rr][cc], dist) < dists[rr][cc]:
                    dists[rr][cc] = cdist
                    heappush(pq, (cdist, rr, cc))
        return dists[m - 1][n - 1]


grid = [
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6],
]
ans = Solution().swimInWater(grid)
print(ans)
