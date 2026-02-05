from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j = j + 1
            elif nums[i] == nums[i-1] and count <= 2:
                nums[j] = nums[i]
                j = j + 1
                count += 1
        print(nums)

nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums))
