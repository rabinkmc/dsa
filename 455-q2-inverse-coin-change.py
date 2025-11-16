from typing import List
from functools import lru_cache


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        self.coins = []

        self.memo = {}

        def dp(i, amt):
            if (i, amt) in self.memo:
                return self.memo[(i, amt)]
            if i >= len(self.coins):
                return 0
            if amt == 0:
                return 1
            if amt < 0:
                return -1

            if self.coins[i] > amt:
                ans = dp(i + 1, amt)
                self.memo[(i, amt)] = ans
                return ans
            else:
                use = dp(i, amt - self.coins[i])
                skip = dp(i + 1, amt)
                ans = use + skip
                self.memo[(i, amt)] = ans
                return ans

        self.coins = []
        for i, ways in enumerate(numWays):
            self.memo = dict()
            calc = dp(0, i + 1)
            if calc == ways:
                continue
            if calc == ways - 1:
                self.coins.append(i + 1)
            else:
                return []
        return self.coins


numWays = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
# numWays = [1, 2, 2, 3, 4]
# numWays = [1, 0]
print(Solution().findCoins(numWays))
