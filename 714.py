from typing import List


"""
For each day i, we calculate the new hold value. We have two options:

We continue holding the stock from the previous day (hold remains the same).
We buy the stock on the current day, so we subtract the stock price at day i from the profit we could have had if we sold the stock on the previous day (sell - prices[i]).

The goal is to maximize the profit while holding the stock, so we choose the maximum value between the two options.

For each day i, we calculate the new sell value. We have two options:

    We continue not holding any stock, and the profit is the same as the previous day (sell remains the same).
    We sell the stock on the current day, so we add the stock price at day i to the profit we could have had if we held the stock on the previous day (hold + prices[i] - fee).

The goal is to maximize the profit while not holding any stock, so we choose the maximum value between the two options.
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        sell = 0
        for i in range(1, len(prices)):
            hold = max(hold,  sell - prices[i])
            sell = max(sell, hold + prices[i] - fee)
        return sell

prices = [1, 3, 2,8,4,9]
print(Solution().maxProfit(prices, 2))
