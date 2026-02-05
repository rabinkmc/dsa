from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        a, b = points[0]
        count = 1
        for start, end in points[1:]:
            if start <= b:
                a, b = [max(start, a), min(end, b)]
            else:
                count += 1
                a, b = start, end
        return count


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
ans = Solution().findMinArrowShots(points)
print(ans)
