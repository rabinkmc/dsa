from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        coins.sort()
        def numCoins(coins, amount):
            if amount in self.memo:
                return self.memo[amount]

            if amount == 0:
                return 0
            if amount < 0:
                return -1

            ans = inf
            for coin in coins:
                 if coin > amount:
                    break
                 no_of_coins = numCoins(coins, amount-coin)
                 if no_of_coins == -1:
                     continue
                 ans = min(ans, 1 + no_of_coins)
            self.memo[amount] = -1 if ans == inf else ans
            return self.memo[amount]
        return numCoins(coins, amount)

ans = Solution().coinChange([1, 2, 3, 4], 4)
print(ans)
