from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1]
        n = len(nums)
        temp = 1
        for i in range(1, n):
            temp *= nums[i-1]
            prod.append(temp)

        temp = 1
        for i in range(n-2, -1, -1):
            temp *= nums[i+1]
            prod[i] *= temp
        return prod
        
nums = [1, 2, 3, 4]
prod = Solution().productExceptSelf(nums)
print(prod)
