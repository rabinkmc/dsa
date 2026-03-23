from typing import List
from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(r, c):
            if cache[r][c] != 0:
                return cache[r][c]
            for dx, dy in dirs:
                rr, cc = r + dx, c + dy
                if rr < 0 or rr >= m or cc < 0 or cc >= n:
                    continue
                if matrix[rr][cc] <= matrix[r][c]:
                    continue
                cache[r][c] = max(cache[r][c], dfs(rr, cc))
            cache[r][c] += 1
            return cache[r][c]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans

matrix = [[9,9,4],[6,6,8],[2,1,1]]
ans = Solution().longestIncreasingPath(matrix)
print(ans)
