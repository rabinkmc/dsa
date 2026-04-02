from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
ans = Solution().lengthOfLIS(nums)
print(ans)
