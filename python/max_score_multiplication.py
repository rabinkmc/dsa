from typing import List
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        @lru_cache(None)
        def dp(i, left):
            if i == m:
                return 0
            # number of operations on the right
            right = n - (i - left) - 1
            lval = multipliers[i] * nums[left]
            rval = multipliers[i] * nums[right]
            return max(lval + dp(i + 1, left + 1), rval + dp(i + 1, left))

        return dp(0, 0)


nums = [1, 2, 3]
multipliers = [3, 2, 1]
ans = Solution().maximumScore(nums, multipliers)
print(ans)
