from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        merged = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = Solution().merge(intervals) 
print(ans)
