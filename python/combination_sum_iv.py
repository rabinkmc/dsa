from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(target):
            if target < 0:
                return 0
            if target == 0:
                return 1
            total = 0
            for num in nums:
                total += dp(target - num)
            return total

        return dp(target)


nums = [1, 2, 3]
target = 4
ans = Solution().combinationSum4(nums, target)
print(ans)
