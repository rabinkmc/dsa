from typing import List

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
