from typing import List
from collections import deque
from functools import lru_cache


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + stones[i]

        def rsum(i, j):
            return psum[j + 1] - psum[i]

        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                case1 = rsum(i, j) - stones[i] - dp[i + 1][j]
                case2 = rsum(i, j) - stones[j] - dp[i][j - 1]
                dp[i][j] = max(case1, case2)

        return dp[0][n - 1]


stones = [5, 3, 1, 4, 2]
stones = [7, 90, 5, 1, 100, 10, 10, 2]
ans = Solution().stoneGameVII(stones)
print(ans)
