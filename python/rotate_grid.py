from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])


grid = [[40, 10], [30, 20]]
k = 1
ans = Solution().rotateGrid(grid, k)
print(ans)
