from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [ defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                    
                dp[i][diff] += cnt + 1
                ans += cnt
        return ans
                
