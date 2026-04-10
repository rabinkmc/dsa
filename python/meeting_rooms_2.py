from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort()
        e1 = intervals[0][1]
        for s2, e2 in intervals[1:]:
            if s2 < e1:
                ans += 1
            else:
                e1 = e2
        return ans


intervals = [[0, 30], [5, 10], [15, 20]]
ans = Solution().minMeetingRooms(intervals)
print(ans)
