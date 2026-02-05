from typing import List
from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        def diag_length(a, b):
            return sqrt(a*a + b*b)
        m, n = dimensions[0] 
        l = diag_length(m, n)
        ans = m*n
        for a, b in dimensions[1:]:
            lc = diag_length(a, b)
            if lc > l:
                l = lc
                ans = a * b
            elif lc == l:
                ans = max(ans, a*b)
        return ans

dimensions = [[9,3],[8,6]]
ans = Solution().areaOfMaxDiagonal(dimensions)
print(ans)
