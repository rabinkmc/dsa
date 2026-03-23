from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
            if dp[target]:
                break
        for j in range(target, -1, -1):
            if dp[j]:
                return S - 2 * j
        return -1


stones = [2, 7, 4, 1, 8, 1]
ans = Solution().lastStoneWeightII(stones)
print(ans)
