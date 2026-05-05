from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        @lru_cache(None)
        def dp(i, csum):
            if csum < 0:
                return False
            if csum == 0:
                return True
            if i == n:
                return csum == 0
            pick = dp(i + 1, csum - nums[i])
            skip = dp(i + 1, csum)
            return pick or skip

        return dp(0, target)


nums = [1, 5, 11, 5]
ans = Solution().canPartition(nums)
print(ans)
