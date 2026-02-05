from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0 
        for i, num in enumerate(nums):
            if num != val:
                nums[j] = num
                j += 1
        return j

nums = [0,1,2,2,3,0,4,2]
val = 2

print(Solution().removeElement(nums, val))
