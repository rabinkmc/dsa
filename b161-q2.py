from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(r, c):
            visited[r][c] = True
            stack = [(r, c)]
            total = 0
            while stack:
                x, y = stack.pop()
                total += grid[x][y]
                dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in dd:
                    rr, cc = x + dx, y + dy
                    if rr < 0 or cc < 0 or rr >= m or cc >= n or visited[rr][cc] or grid[rr][cc] == 0:
                        continue
                    visited[rr][cc] = True
                    stack.append((rr, cc))
            return total

        ans = 0
        for r in range(m):
            for c in range(n):
                if visited[r][c] or grid[r][c] == 0:
                    continue
                rv = dfs(r, c)
                if rv % k == 0:
                    ans += 1
        return ans

grid = [
    [0,2,1,0,0],
    [0,5,0,0,5],
    [0,0,1,0,0],
    [0,1,4,7,0],
    [0,2,0,0,8]
]

ans = Solution().countIslands(grid, 5)
print(ans)
        
