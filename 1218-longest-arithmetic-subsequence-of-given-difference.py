from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        ans = 0
        for num in arr:
            dp[num] = 1 + dp.get(num - difference, 0)
            ans = max(dp[num], ans)
        return ans




arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
print(Solution().longestSubsequence(arr=arr, difference=-2))
