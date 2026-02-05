from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        def max_local(r, c):
            ans = 0
            for i in range(r, r+3):
                for j in range(c, c+3):
                    ans = max(ans, grid[i][j])
            return ans


        ans = []
        for i in range(n-2):
            res = []
            for j in range(n-2):
                res.append(max_local(i, j))
            ans.append(res)
        return ans
        
