from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modPrefix = 0
        lookup = {0: -1}
        for index, num in enumerate(nums):
            modPrefix = (modPrefix + num) % k
            if modPrefix in lookup:
                if index - lookup[modPrefix] > 1:
                    return True
            else:
                lookup[modPrefix] = index
        return False


nums = [23, 2, 6, 4, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))
