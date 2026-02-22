from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            i = i + 1
        out = [x for x in nums if x != 0]
        out.extend([0] * (n - len(out)))
        return out


nums = [1, 2, 2, 1, 1, 0]
print(Solution().applyOperations(nums))
