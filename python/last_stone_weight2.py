from heapq import heappop, heappush
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for stone in stones:
            heappush(pq, -stone)
        while len(pq) > 1:
            a = -heappop(pq)
            b = -heappop(pq)
            if a > b:
                heappush(pq, -(a - b))
        if len(pq):
            return -pq[0]
        return 0

stones = [2, 7, 4, 1,8, 1]
ans = Solution().lastStoneWeight(stones)
print(ans)
