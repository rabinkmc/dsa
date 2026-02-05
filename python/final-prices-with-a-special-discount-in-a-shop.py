from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            if stack:
                res[i] = prices[i] - prices[stack[-1]]
            else:
                res[i] = prices[i]
            stack.append(i)
        return res


prices = [8,4,6,2,3]
print(Solution().finalPrices(prices))
