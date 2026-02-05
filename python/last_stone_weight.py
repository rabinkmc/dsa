from typing import List
from heapq import heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []
        for stone in stones:
            heappush(q, -stone)

        while len(q) > 1:
            y = -heappop(q)
            x = -heappop(q)
            if y != x:
                heappush(q, -(y - x))
        if q:
            return -q[0]
        return 0


stones = [2, 7, 4, 1, 8, 1]
ans = Solution().lastStoneWeight(stones)
print(ans)
