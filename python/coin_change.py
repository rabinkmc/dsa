from typing import List
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        INF = float("inf")

        @lru_cache(None)
        def dp(i, rem):
            if rem == 0:
                return 0
            if i == len(coins):
                return INF

            skip = dp(i + 1, rem)
            take = INF
            if coins[i] <= rem:
                take = 1 + dp(i, rem - coins[i])
            return min(take, skip)

        res = dp(0, amount)
        if res == INF:
            return -1
        return res


coins = [1, 2, 5]
amount = 11
# coins = [1]
# amount = 1
# coins = [2]
# amount = 3
ans = Solution().coinChange(coins, amount)
print(ans)
