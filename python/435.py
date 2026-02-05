from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        output = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                output += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return output


intervals = [[1, 2], [1, 10], [2, 3], [3, 4], [1, 3]]
ans = Solution().eraseOverlapIntervals(intervals)
print(ans)

"""
end = 2

1-2 1-3 1-10 2-3 3-4
end = 2 (1-2) (1-3) ( +1 )
end = 3 (1-2) (2-3)
end = 4 (2-3) (3-4)
"""
