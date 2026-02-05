from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            m = left + (right - left) // 2
            if nums[m] > nums[-1]:
                left = m + 1
            else:
                idx = m
                right = m - 1

        # now we search in the left and right half of the index
        # there are two halves
        # first half 0:idx
        # second half idx:

        if nums[0] <= target <= nums[idx - 1]:
            left = 0
            right = idx - 1
        else:
            left = idx
            right = len(nums) - 1

        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 7
ans = Solution().search(nums, target)
print(ans)
