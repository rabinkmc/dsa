 # 2739. Total Distance Traveled
from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            diff = min(nums[i] - nums[i-1], diff)
        return diff

nums = [100, 1, 10]
ans = Solution().findValueOfPartition(nums)
print(ans)

        
