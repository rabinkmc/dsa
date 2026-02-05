from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        output = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                return output + [newInterval] + intervals[i:]
            elif newInterval[0] > interval[1]:
                output.append(interval)
            else:
                newInterval = [
                    min(interval[0], newInterval[0]), max(interval[1], newInterval[1])
                ]
        return output + [newInterval]


solution = Solution()
interval = [[1,2],[3,5],[6,7],[8,10],[12,16]]
ans = solution.insert(interval, [4, 8])
assert ans == [[1, 2], [3, 10], [12, 16]], ans
