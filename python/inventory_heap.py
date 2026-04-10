from collections import Counter
from typing import List


def serial_sum(a, b):
    return (b - a + 1) * (a + b) // 2


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 1_000_000_007
        inventory.append(0)
        orders_left = orders
        profit = 0
        counter = Counter(inventory)
        items = [[key, freq] for key, freq in counter.items()]
        items.sort(reverse=True)
        n = len(items)
        for i in range(n):
            nex = items[i + 1][0]
            curr = items[i][0]
            buffer = (curr - nex) * items[i][1]
            if buffer <= orders:
                start = nex + 1
                profit = profit + serial_sum(start, curr) * items[i][1]
                orders = orders - buffer
                if orders == 0:
                    return profit % MOD
                items[i + 1][1] = items[i + 1][1] + items[i][1]
            else:
                layers = orders // items[i][1]
                mult = orders
                start = curr - layers + 1
                rem = orders % items[i][1]
                if layers > 0:
                    profit = (profit + serial_sum(start, curr) * items[i][1]) % MOD
                next_price = curr - layers
                profit = (profit + rem * next_price) % MOD
                return profit % MOD

        return profit % MOD


inventory = [1000, 1000]
orders = 2
ans = Solution().maxProfit(inventory, orders)
print(ans)
