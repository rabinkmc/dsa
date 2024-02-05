from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def check(i, j):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if (x1 != x2 ):
                if (y2 - y1) / ( x2 - x1) > 0:
                    return False
            for a in range(min(x1, x2), max(x1, x2) + 1):
                for b in range(min(y1, y2), max(y1, y2) + 1):
                    if ([a,b] == points[i] or [a,b] == points[j]):
                        continue
                    if [a,b] in points:
                        return False
            return True
        # points.sort(key= lambda x: (-x[1], x[0]))
        n = len(points)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                count += int(check(i, j))
        return count

points = [[6,2],[4,4],[2,6]]
ans = Solution().numberOfPairs(points)
print(ans)
        
