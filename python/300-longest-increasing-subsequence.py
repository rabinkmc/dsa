from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

nums = [4,10,4,3,8,9]
solution = Solution().lengthOfLIS(nums)
assert solution == 3
solution = Solution().lengthOfLIS(nums)
nums = [10,9,2,5,3,7,101,18]
assert solution == 4
            


        
        
