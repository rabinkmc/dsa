from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        res = [0]*len(nums)
        while i <= j:
            while abs(nums[j]) > abs(nums[i]):
                res[k] = nums[j] * nums[j]
                j -= 1
                k -= 1
            else:
                res[k] = nums[i] * nums[i]
                i += 1
                k -= 1
        return res

ans = Solution().sortedSquares([-3, -2, 0, 1, 3, 9])
print(ans)
        
