from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        self.group = []

        def dfs(r, c):
            self.group.append((r, c))
            grid2[r][c] = -1
            dd = [(1, 0), (0, 1), (-1, 0)]
            for dx, dy in dd:
                rr, cc = r + dx, c + dy
                if rr < 0 or rr >= m or cc < 0 or cc >= n:
                    continue
                if grid2[rr][cc] == 1:
                    dfs(rr, cc)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    self.group = []
                    dfs(i, j)
                    valid = True
                    for r, c in self.group:
                        if grid1[r][c] != 1:
                            valid = False
                            break
                    if valid:
                        count += 1
        return count


grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
]
ans = Solution().countSubIslands(grid1, grid2)
print(ans)
