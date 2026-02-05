from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        we flood fill all the 1's from the boundary to 0
        then count the remaining 1's

        so beautiful
        """
        m = len(grid)
        n = len(grid[0])

        # b1 = boundary one
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid[r][c] == 0:
                return
            # logic
            grid[r][c] = 0
            # logic
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        dfs(i, j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
        return ans


grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
grid = [
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
]
ans = Solution().numEnclaves(grid)
print(ans)
