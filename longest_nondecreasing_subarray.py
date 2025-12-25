from typing import List
from functools import lru_cache


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(i, k, prev):
            if i == n:
                return 0
            length = 0
            while i < n and nums[i] >= prev:
                prev = nums[i]
                i += 1
                length += 1
            else:
                casea = length
                if k == 0:
                    casea += 1 + dfs(i + 1, 1, prev)
                # otherwise we start a new array
                caseb = -1
                if i < n:
                    caseb = dfs(i, 0, nums[i])
                return max(casea, caseb)

        return dfs(0, 0, nums[0])


nums = [1, 2, 0, 4, 3]
print(Solution().longestSubarray(nums))
