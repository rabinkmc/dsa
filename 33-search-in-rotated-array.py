from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        i = 0
        while left <= right:
            m = (left + right) // 2
            if nums[m] > nums[-1]:
                left = m + 1
            else:
                i = m
                right = m - 1
        # now I need to search on two halves
        # either from 0 to i-1, or from i to s
        left = 0
        right = len(nums) - 1
        if target == nums[i]:
            return i
        if nums[i] < target <= nums[-1]:
            left = i
        else:
            right = i
        ans = -1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return ans


solution = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
assert solution == 4
solution = Solution().search(nums=[3, 1], target=3)
assert solution == 0, "solution 2"
solution = Solution().search(nums=[5, 1, 3], target=1)
assert solution == 1, "solution 3"
