from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        for coin in coins:
            dp[coin] += 1
        for x in range(amount + 1):
            for coin in coins:
                if coin > x:
                    continue
                dp[x] += dp[x - coin]
        print(dp)
        return dp[amount]


amount = 5
coins = [1, 2, 5]
ans = Solution().change(amount, coins)
print(ans)
