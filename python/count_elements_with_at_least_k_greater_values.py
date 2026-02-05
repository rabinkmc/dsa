from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        if k == 0:
            return n

        @lru_cache(None)
        def bsearch(target):
            ans = -1
            left = 0
            right = n - 1
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] > target:
                    ans = m
                    right = m - 1
                else:
                    left = m + 1
            return ans

        res = 0
        for num in nums:
            idx = bsearch(num)
            if idx == -1:
                continue
            if n - idx >= k:
                res += 1
        return res


nums = [1, 2, 2, 4, 4, 5]
nums = [5, 5, 5]
k = 2
# k = 1
print()
ans = Solution().countElements(nums, k)
print(ans)
