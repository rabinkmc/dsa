from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(None)
        def dp(i, amt):
            if i == len(coins):
                if amt == 0:
                    return 1
                else:
                    return 0
            skip = dp(i + 1, amt)
            take = 0
            if coins[i] <= amt:
                take = dp(i, amt - coins[i])
            return take + skip

        return dp(0, amount)


amount = 5
coins = [1, 2, 5]
ans = Solution().change(amount, coins)
print(ans)
