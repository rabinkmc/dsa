# https://leetcode.com/contest/weekly-contest-323/problems/delete-greatest-value-in-each-row/
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        sort each row, 
        transpose, pick the max of each row and add
        """
        for row in grid:
            row.sort()

        gridt = list(zip(*grid))
        total = 0
        for row in gridt:
            total += max(row)
                
        return total

grid = [[1,2,4],[3,3,1]]
ans = Solution().deleteGreatestValue(grid)
print(ans)
