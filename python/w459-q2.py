from typing import List
import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        ys = dict()
        for _, y in points:
            ys[y] = ys.get(y, 0) + 1
        combinations = []
        for count in ys.values():
            if count < 2:
                continue
            yc2 = math.comb(count, 2)
            combinations.append(yc2)

        ans = 0
        e = 1000_000_007
        suffix = sum(combinations)
        for comb in combinations:
            suffix -= comb
            ans += (comb * suffix) % e
        return ans % e

points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
points  = [[-73,-72],[-1,-56],[-92,30],[-57,-89],[-19,-89],[-35,30],[64,-72]]
ans = Solution().countTrapezoids(points)
print(ans)
        
