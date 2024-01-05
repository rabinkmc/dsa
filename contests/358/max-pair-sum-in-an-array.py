from typing import List

nums = [32,13,74,473,42]

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n):
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]
                if max(str(a)) == max(str(b)):
                    ans = max(ans, a + b)
        return ans
                    

ans = Solution().maxSum(nums)
print(ans)

        
