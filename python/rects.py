from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rects = [min(x) for x in rectangles]
        return rects.count(max(rects))


ans = Solution().countGoodRectangles(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]])
print(ans)
