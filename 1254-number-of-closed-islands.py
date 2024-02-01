from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                # change boundary land to water
                grid[r][c] = 1
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr >= m or cc < 0 or cc >= n or grid[rr][cc] == 1: 
                        continue
                    stack.append((rr, cc))
        


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    dfs(i, j)
        count = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
ans = Solution().closedIsland(grid)
print(ans)
