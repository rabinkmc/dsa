from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if -nums[i] in seen:
                return nums[i]
        return -1


nums = [-1, 2, -3, 3]
ans = Solution().findMaxK(nums)
