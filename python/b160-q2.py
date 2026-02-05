from typing import List
from functools import lru_cache


class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        INF = float("inf")
        memo = dict()

        def dfs(i, j, parity):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= m or j >= n:
                return INF
            if i == m - 1 and j == n - 1:
                return m * n
            if parity == 1 or (i == 0 and j == 0):
                ans = (i + 1) * (j + 1) + min(dfs(i, j + 1, 0), dfs(i + 1, j, 0))
                memo[(i, j)] = ans
                return ans
            ans = waitCost[i][j] + dfs(i, j, 1)
            memo[(i, j)] = ans
            return ans

        return dfs(0, 0, 0)


m = 1
n = 2
waitCost = [[1, 2]]
m = 2
n = 2
waitCost = [[3, 5], [2, 4]]
ans = Solution().minCost(m, n, waitCost)
print(ans)
