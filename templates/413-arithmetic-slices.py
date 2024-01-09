from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        i = 2
        ans = 0
        while i < len(nums):
            count = 1
            a = nums[i-2]
            b = nums[i-1]
            d = b - a
            while i < len(nums) and (b + count*d == nums[i]):
                count += 1
                i = i + 1
            else:
                ans += count * (count - 1) // 2
                i = i + 1
        return ans
    
    def calc(self, count):
        return (count * (count + 1))//2

nums = [1, 2, 3, 4, 5, 9, 13, 17, 21, 27, 33, 36, 39, 40, 41, 42, 43, 44, 45]
ans = Solution().numberOfArithmeticSlices(nums)
print(ans)
