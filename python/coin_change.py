from typing import List
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()

        @lru_cache(None)
        def dp(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0

            ans = float("inf")
            for coin in coins:
                if rem - coin < 0:
                    break
                nc = dp(rem - coin)
                if nc == -1:
                    continue
                ans = min(ans, 1 + nc)
            if ans == float("inf"):
                return -1
            return ans

        return dp(amount)


coins = [1, 2, 5]
amount = 11
# coins = [1]
# amount = 1
ans = Solution().coinChange(coins, amount)
print(ans)
