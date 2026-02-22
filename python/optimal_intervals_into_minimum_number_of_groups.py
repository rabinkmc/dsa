from typing import List
from heapq import heappush, heappop


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        free = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] > free[0]:
                heapq.heapop(free)
            heapq.heappush(free, interval[1])
        return len(free)


intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
ans = Solution().minGroups(intervals)
print(ans)
