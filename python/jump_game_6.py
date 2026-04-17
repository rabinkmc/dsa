from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dq = deque()
        dq.append(0)
        for i in range(1, n):
            if dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + dp[dq[0]]
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            dq.append(i)
        return dp[-1]


nums = [1, -1, -2, 4, -7, 3]
k = 2
nums = [1, -5, -20, 4, -1, 3, -6, -3]
k = 2
ans = Solution().maxResult(nums, k)
print(ans)
