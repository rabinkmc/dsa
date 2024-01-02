from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        for num in nums:
            if num == "0":
                red += 1
            elif num == "1":
                white += 1
        print(red, white)
        i = 0
        while i < red:
            nums[i] = 0
            i += 1
        while i < red + white:
            nums[i] = 1
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1

nums = ["2", "2" , "2" , "1" , "1", "2", "0", "0", "1"]
Solution().sortColors(nums)
        
