from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j = j + 1
        return j

nums = [1, 1, 1, 2, 2, 3]

print(Solution().removeDuplicates(nums))


