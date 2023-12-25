from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        profit = 0
        for i in range(1, len(prices)):
            hold = max(hold, profit - prices[i])
            profit = max(profit, hold + prices[i])
        return profit
prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
