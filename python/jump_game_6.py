from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[max(0, i - k) : i]) + nums[i]
        return dp[n - 1]


nums = [1, -1, -2, 4, -7, 3]
k = 2
# nums = [1, -5, -20, 4, -1, 3, -6, -3]
# k = 2
ans = Solution().maxResult(nums, k)
print(ans)
