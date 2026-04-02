from typing import List
from heapq import heappop, heappush


def serial_sum(a, b):
    return (b - a + 1) * (a + b) // 2


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 1_000_000_007
        pq = []
        n = len(inventory)
        for item in inventory:
            heappush(pq, -item)
        orders_left = orders
        profit = 0
        count = 0
        print(pq)
        while orders_left > 0:
            if count == 10:
                break
            max_corder = -heappop(pq)
            # possible orders that can be processed depends
            top = -pq[0] if pq else 0
            corder = 0
            if max_corder > top:
                corder = min(max_corder - top, orders_left)
                heappush(pq, -(max_corder - corder))
            elif max_corder == top:
                corder = min(top, orders_left)

            orders_left = orders_left - corder
            # now it is time to compute the profit
            # that means
            end = max_corder
            start = max_corder - corder + 1
            profit = (profit + serial_sum(start, end)) % MOD
            print(pq, corder, profit, orders_left)
            count += 1

        return profit


inventory = [3, 5]
orders = 6
ans = Solution().maxProfit(inventory, orders)
print(ans)
