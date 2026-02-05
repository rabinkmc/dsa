from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        ans = float('-inf')
        for num in nums:
            total += num
            ans = max(ans, total)
            total = max(total, 0)
        return ans


solution = Solution()
ans = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
assert ans == 6, ans
        

