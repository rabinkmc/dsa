from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        e1 = intervals[0][1]
        for s2, e2 in intervals[1:]:
            if s2 < e1:
                ans += 1
                e1 = min(e1, e2)
            else:
                e1 = e2
        return ans


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
ans = Solution().eraseOverlapIntervals(intervals)
print(ans)
