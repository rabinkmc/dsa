from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1
        ans = -1
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] > nums[-1]:
                left = m + 1
            else:
                ans = m 
                right = m - 1
        return nums[ans]
        
nums = [3, 4, 5, 6, 0, 1, 2]
solution = Solution().findMin(nums)
assert solution == 0, solution
