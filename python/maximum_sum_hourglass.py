from typing import List


def hour_glass_sum(grid, r, c):
    total = 0
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            total += grid[i][j]
    cx, cy = r + 1, c + 1
    left = grid[cx][cy - 1]
    right = grid[cx][cy + 1]
    return total - (left + right)


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = -1 * 1000_000 * 150 * 150
        for i in range(m - 3 + 1):
            for j in range(n - 3 + 1):
                ans = max(ans, hour_glass_sum(grid, i, j))
        return ans


grid = [[6, 2, 1, 3], [4, 2, 1, 5], [9, 2, 8, 7], [4, 1, 2, 9]]
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = Solution().maxSum(grid)
print(ans)
