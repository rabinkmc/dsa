from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def dp(i, amt):
            if i == n:
                return 0
            if amt < 0:
                return 0
            if amt == 0:
                return 1
            if coins[i] > amt:
                return dp(i + 1, amt)
            else:
                return dp(i, amt - coins[i]) + dp(i + 1, amt)

        return dp(0, amount)


print(Solution().change(5, [1, 2, 5]))
