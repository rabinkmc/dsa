from typing import List

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] > nums[i-1]:
            i = i - 1
        return i

nums = [1,-1,2,3,3,4,5]
nums = [1, 2, 3, 4, -0, 1, 2, 3]
ans = Solution().minimumPrefixLength(nums)
print(ans)
