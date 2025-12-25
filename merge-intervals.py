from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        out = [intervals[0]]
        for i in range(1, n):
            s1, e1 = out[-1]
            s2, e2 = intervals[i]
            if e1 >= s2:
                out[-1] = [s1, max(e1, e2)]
            else:
                out.append([s2, e2])

        return out


intervals = [[4, 7], [2, 6], [8, 10], [15, 18]]
ans = Solution().merge(intervals)
print(ans)
