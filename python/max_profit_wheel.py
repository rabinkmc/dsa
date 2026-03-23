from typing import List

class Solution:
    def minOperationsMaxProfit(
        self, 
        customers: List[int],
        boardingCost: int,
        runningCost: int
    ) -> int:
        boarded = 0
        count = 0
        max_profit = -1
        ans = -1
        waiting = 0
        for customer in customers:
            count += 1
            waiting += customer
            board_now = min(4, waiting)
            waiting -= board_now
            boarded += board_now
            profit = boarded * boardingCost - count * runningCost
            if profit > max_profit:
                max_profit = profit
                ans = count
        while waiting > 0:
            count += 1
            board_now = min(4, waiting)
            waiting -= board_now
            boarded += board_now
            profit = boarded * boardingCost - count * runningCost
            if profit > max_profit:
                ans = count
                max_profit = profit
        if max_profit > 0:
            return ans
        else:
            return -1

customers = [8,3]
boardingCost = 5
runningCost = 6

ans = Solution().minOperationsMaxProfit(
    customers,
    boardingCost,
    runningCost
)
print(ans)
        
