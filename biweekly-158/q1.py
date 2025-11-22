from typing import List

class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        map = dict()
        n = len(x)
        for i in range(n):
            xi = x[i]
            yi = y[i]
            if (xi not in map) or map[xi] < yi:
                map[xi] = yi
        values = sorted(map.values(), reverse=True)
        if len(values) < 3:
            return -1
        else:
            return sum(values[0:3])

