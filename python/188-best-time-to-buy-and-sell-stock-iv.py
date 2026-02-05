from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i, holding):
            if i >= n:
                return 0

            nothing = dp(i + 1, holding)
            selling = prices[i] + dp(i + 2, 0)
            buying = -prices[i] + dp(i + 1, 1)
            if holding:
                return max(nothing, selling)
            else:
                return max(nothing, buying)

        return dp(0, 0)


print(Solution().maxProfit(prices=[1]))
