from typing import List
from collections import defaultdict


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        If there are no next nodes we have reached the end of the path
        and now we should evaluate the total
        """
        m = len(grid)
        n = len(grid[0])
        self.answer = 0

        def next_node(r, c, path):
            neighbors = []
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                rr, cc = r + dr, c + dc
                if rr < 0 or rr >= m or cc < 0 or cc >= n:
                    continue
                if (rr, cc) in path or grid[rr][cc] == 0:
                    continue
                neighbors.append((rr, cc))
            return neighbors


        def dfs(r, c, path):
            neighbors = next_node(r, c, path)
            if not neighbors:
                total = 0
                for i, j in path:
                    total += grid[i][j]
                self.answer = max(self.answer, total)
                return 

            for rr, cc in neighbors:
                dfs(rr, cc, path + [(rr, cc)])

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    dfs(r, c, [(r, c)])
        return self.answer


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
ans = Solution().getMaximumGold(grid)
print(ans)
