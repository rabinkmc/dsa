from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def dp(i, csum):
            if i == n and csum == target:
                return 1
            if i == n:
                return 0
            plus = dp(i + 1, csum + nums[i])
            minus = dp(i + 1, csum - nums[i])
            return plus + minus

        return dp(0, 0)


nums = [1, 1, 1, 1, 1]
target = 3
ans = Solution().findTargetSumWays(nums, target)
print(ans)
