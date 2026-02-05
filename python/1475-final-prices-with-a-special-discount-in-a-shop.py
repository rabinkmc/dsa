from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discounts = []
        for i in range(n):
            price = prices[i]
            discount = 0
            for j in range(i+1, n):
                if prices[j] <= price: 
                    discount = prices[j]
                    break
            discounts.append(price - discount)
        return discounts
        
prices = [8,4,6,2,3]
ans = Solution().finalPrices(prices)
print(ans)
