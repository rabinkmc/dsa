from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        out = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            e1 = out[-1][1]
            s2, e2 = intervals[i]
            if s2 < e1:
                out[-1][1] = max(e1, e2)
            else:
                out.append([s2, e2])
        return out


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
ans = Solution().insert(intervals, newInterval)
print(ans)
