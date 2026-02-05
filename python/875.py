from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        result = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canFinish(piles, h, mid):
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return result

    def canFinish(self, piles, h, k):
        time = 0
        for pile in piles:
            time += (pile / k).__ceil__()
        return time <= h


piles = [3, 6, 7, 11]
h = 8
print(Solution().minEatingSpeed(piles, h))
