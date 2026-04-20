from typing import List
from heapq import heappush, heappop


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell = []
        buy = []
        n = len(orders)
        for i in range(n):
            price, amt, t = orders[i]
            if t == 0:
                while amt > 0 and sell and price >= sell[0][0]:
                    sp, sell_amt = heappop(sell)
                    if sell_amt <= amt:
                        amt -= sell_amt
                    else:
                        heappush(sell, (sp, sell_amt - amt))
                        amt = 0
                if amt > 0:
                    heappush(buy, (-price, amt))
            if t == 1:
                while amt > 0 and buy and price <= -buy[0][0]:
                    cp, buy_amt = heappop(buy)
                    if buy_amt <= amt:
                        amt -= buy_amt
                    else:
                        heappush(buy, (cp, buy_amt - amt))
                        amt = 0
                if amt > 0:
                    heappush(sell, (price, amt))
        ans = 0
        for order in buy:
            ans += order[1]
        for order in sell:
            ans += order[1]
        return ans % 1_000_000_007


orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
ans = Solution().getNumberOfBacklogOrders(orders)
print(ans)
