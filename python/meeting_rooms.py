from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        e1 = intervals[0][1]
        for s2, e2 in intervals[1:]:
            if s2 < e1:
                return False
            else:
                e1 = e2
        return True


intervals = [[0, 30], [5, 10], [15, 20]]
intervals = [[7, 10], [2, 4]]
ans = Solution().canAttendMeetings(intervals)
print(ans)
