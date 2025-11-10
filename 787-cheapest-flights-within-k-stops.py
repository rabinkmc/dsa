from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        queue = deque()
        cost, step = 0, 0
        queue.append((src, cost, step))
        ans = 10000000
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        found = False
        prices = [float("inf") for _ in range(n)]
        prices[src] = 0

        while queue:
            node, cost, step = queue.popleft()
            if step > k + 1:
                continue
            if node == dst:
                ans = min(ans, cost)
                found = True
                continue

            for adj, w in graph[node]:
                new_price = cost + w
                if prices[adj] > new_price:
                    prices[adj] = new_price
                    queue.append((adj, new_price, step + 1))

        return ans if found else -1


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
