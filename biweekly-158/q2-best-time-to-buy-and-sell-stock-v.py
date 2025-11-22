from typing import List
from functools import lru_cache


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        FREE = 0
        LONG = 1
        SHORT = 2

        n = len(prices)

        @lru_cache(None)
        def dp(i, txn, state):
            if i == n:
                if txn == 0 and state == FREE:
                    return 0
                return -float("inf")

            if state == LONG:
                sold = prices[i] + dp(i + 1, txn - 1, FREE)
                do_nothing = dp(i + 1, txn, LONG)
                return max(sold, do_nothing)
            elif state == SHORT:
                buy = -prices[i] + dp(i + 1, txn - 1, FREE)
                do_nothing = dp(i + 1, txn, SHORT)
                return max(buy, do_nothing)
            else:
                sold = prices[i] + dp(i + 1, txn, SHORT)
                buy = -prices[i] + dp(i + 1, txn, LONG)
                do_nothing = dp(i + 1, txn, FREE)
                return max(buy, sold, do_nothing)

        return dp(0, k, FREE)


prices = [12, 16, 19, 19, 8, 1, 19, 13, 9]
prices = [3, 2, 6, 5, 0, 3]
prices = [1, 7, 9, 8, 2]
k = 2
ans = Solution().maximumProfit(prices, k)
print(ans)
