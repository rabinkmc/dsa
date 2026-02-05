from heapq import heappush, heappop
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]

points = [[1,3],[-2,2]]
k = 1       
ans = Solution().kClosest(points, k)
print(ans)
