from functools import lru_cache


class Solution:
    def numWays(self, n: int, k: int) -> int:
        @lru_cache(None)
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k * k
            return (dp(i - 1) + dp(i - 2)) * (k - 1)

        return dp(n)


n = 3
k = 2
print(Solution().numWays(n, k))
