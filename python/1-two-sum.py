from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = {}

        for i, num in enumerate(nums):
            if target - num in keys:
                return [keys[target - num], i]
            keys[num] = i
        return [-1, -1]


nums = [3, 2, 4]
target = 6
nums = [3, 3]
target = 6
print(Solution().twoSum(nums, target))
