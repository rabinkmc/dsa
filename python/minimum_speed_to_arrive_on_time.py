from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(x):
            time = 0
            for d in dist:
                ctime = d / x
                if time + ctime > hour:
                    return False
                time = time + math.ceil(ctime)
            return True

        l = 1
        r = 1000_000_000
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


dist = [1, 3, 2]
hour = 2.7
ans = Solution().minSpeedOnTime(dist, hour)
print(ans)
