from collections import Counter, defaultdict
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        total = defaultdict(int)
        for num in nums:
            total[num] += num

        uniques = list(set(nums))
        uniques.sort()
        n = len(uniques)

        dp = [0]*n
        dp[0] = total[uniques[0]]

        for i in range(1, n):
            curr = uniques[i]
            prev = uniques[i-1]
            if curr - prev == 1:
                dp[i] = max(dp[i-1], dp[i-2] + total[curr])
            else:
                dp[i] = dp[i-1] + total[curr]
        return dp[n-1]

nums = [3, 4, 2]
Solution().deleteAndEarn(nums)

