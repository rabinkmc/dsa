from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        MAX = 10000000
        prices = [MAX for _ in range(n)]
        prices[src] = 0
        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, price in flights:
                tmp[v] = min(tmp[v], prices[u] + price)
            prices = tmp

        return prices[dst] if prices[dst] != MAX else -1


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src, dst, k = 0, 3, 1

# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src, dst, k = 0, 2, 1
#
# n = 3
# flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src, dst, k = 0, 2, 0

# n = 5
# flights = [[1, 0, 5], [2, 1, 5], [3, 0, 2], [1, 3, 2], [4, 1, 1], [2, 4, 1]]
# src = 2
# dst = 0
# k = 2

print(Solution().findCheapestPrice(n, flights, src, dst, k))
