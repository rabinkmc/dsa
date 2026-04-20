from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bucket = [0] * 100000
        for cost in costs:
            bucket[cost] += 1
        ans = 0
        for price, amt in enumerate(bucket):
            if coins > amt * price:
                ans += amt
                coins -= amt * price
            else:
                item = coins // price
                ans += item
                return ans
        return ans


costs = [1, 3, 2, 4, 1]
coins = 7
costs = [10, 6, 8, 7, 7, 8]
coins = 5
ans = Solution().maxIceCream(costs, coins)
print(ans)
