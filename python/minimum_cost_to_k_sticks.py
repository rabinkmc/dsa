from typing import List
from heapq import heappush, heappop

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = []
        for stick in sticks:
            heappush(pq, stick)
        ans = 0
        while len(pq) > 1:
            a = heappop(pq)
            b = heappop(pq)
            cost = a + b
            ans += cost
            heappush(pq, cost)
        return ans

sticks = [2,4,3]
ans = Solution().connectSticks(sticks)
print(ans)
        
