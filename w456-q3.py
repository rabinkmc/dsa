from typing import List


class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pre = [0] * (n + 1)
        curr = 0
        for i in range(n):
            pre[i + 1] = pre[i] ^ nums[i]

        inf = float("inf")
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = pre[i]
        for j in range(2, k + 1):
            for i in range(j, n + 1):
                for t in range(j - 1, i):
                    curr = pre[t] ^ pre[i]
                    res = max(dp[t][j - 1], curr)
                    dp[i][j] = min(dp[i][j], res)
        return dp[n][k]


nums = [1, 2, 3]
k = 2
ans = Solution().minXor(nums, k)
print(ans)
