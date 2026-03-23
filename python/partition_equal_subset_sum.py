from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        cap = total // 2
        dp = [[False] * (cap + 1) for _ in range(n + 1)]
        dp[n][0] = True
        for i in range(n - 1, -1, -1):
            for c in range(0, cap + 1):
                dp[i][c] = dp[i + 1][c] or (c >= nums[i] and dp[i + 1][c - nums[i]])
        return dp[0][cap]


nums = [1, 5, 11, 5]
ans = Solution().canPartition(nums)
print(ans)
