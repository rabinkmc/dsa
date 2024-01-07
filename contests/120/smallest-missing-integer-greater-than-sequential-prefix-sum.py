from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        """
        first find the largest sequential sum
        """
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                break
            total += nums[i]
        while total in nums:
            total += 1
        return total


nums = [14,9,6,9,7,9,10,4,9,9,4,4]
ans = Solution().missingInteger(nums)
print(ans)
