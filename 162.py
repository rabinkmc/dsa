from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)
        while i <= j:
            m = (i + j) // 2
            left = float("-inf") if m - 1 < 0 else nums[m - 1]
            right = float("-inf") if m + 1 >= len(nums) else nums[m + 1]
            if nums[m] > left and nums[m] > right:
                return m
            elif nums[m] < right:
                i = m + 1
            else:
                j = m - 1
        return -1


nums = [1, 2, 1, 3, 5, 6, 4]
nums = [2, 1]
print(Solution().findPeakElement(nums))
