from typing import List
from functools import lru_cache

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        @lru_cache(None)
        def dp(i, j, cost):
            if (i, j) == (0, 0):
                return 0
            left = -1
            score = grid[i][j]
            curr_cost = cost + int(score != 0)
            if curr_cost == k + 1:
                return -1
            if (i >= 0 and j-1 >= 0):
                left = dp(i, j - 1, curr_cost)
            up = -1
            if (i - 1 >= 0 and j >= 0):
                up = dp(i-1, j, curr_cost)
            if left == -1 and  up == -1:
                return -1
            return score + max(left, up)

        return dp(m-1, n-1, 0)


grid = [[0, 1], [1, 2]]
grid = [[0, 1],[2, 0]]
k = 1
print(Solution().maxPathScore(grid, k))
