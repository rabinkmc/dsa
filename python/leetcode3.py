from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        limit = i = 0
        ans = 0
        while limit < target:
            if i < len(coins) and coins[i] <= limit + 1:
                limit += coins[i]
                i += 1
            else:
                print(limit + 1)
                limit = 2 * limit + 1
                ans += 1
        print(ans)
        return 0


coins = [1, 4, 10]
target = 19

Solution().minimumAddedCoins(coins, target)
