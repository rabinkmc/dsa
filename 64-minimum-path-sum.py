from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for c in range(1, n):
            grid[0][c] += grid[0][c-1]

        for r in range(1, m):
            grid[r][0] += grid[r-1][0]

        for i in range(1, m):
            for j in range(1, n):
                    grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
        
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
ans = Solution().minPathSum(grid)
print(ans)
