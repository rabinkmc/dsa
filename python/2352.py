from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = dict()
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            builder = []
            for c in range(n):
                builder.append(str(grid[r][c]))
            key = ",".join(builder)
            rows[key] = rows.get(key, 0) + 1
        ans = 0
        for c in range(n):
            builder = []
            for r in range(m):
                builder.append(str(grid[r][c]))
            key = ",".join(builder)
            if key in rows:
                ans += rows[key]
        return ans

grid = [[3,2,1],[1,7,6],[2,7,7]]
grid = [
    [3,1,2,2],
    [1,4,4,5],
    [2,4,2,2],
    [2,4,2,2]
]
ans = Solution().equalPairs(grid)
print(ans)
        
