from typing import List
from functools import lru_cache


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        psum = [0] * (n)
        psum[0] = stones[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + stones[i]

        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return psum[n - 1]
            take = psum[i] - dp(i + 1)
            skip = dp(i + 1)
            return max(take, skip)

        return dp(1)


stones = [-1, 2, -3, 4, -5]
ans = Solution().stoneGameVIII(stones)
print(ans)
