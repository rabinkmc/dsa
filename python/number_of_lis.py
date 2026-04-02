class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1)
        ans = 0
        max_dp = max(dp)
        return dp.count(max_dp)
