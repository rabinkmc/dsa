from typing import List
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1 
        if nums[right] != target:
            return [-1, -1]
        return [left, right]


nums = [5, 5, 7, 9, 9]
target = 5
ans = Solution().searchRange(nums, target)
print(ans)

 
