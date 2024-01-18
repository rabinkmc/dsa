from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        def topleft(i, j):
            ans = set()
            i = i - 1
            j = j - 1
            while i >= 0 and j >=0:
                ans.add(grid[i][j]) 
                i = i - 1
                j = j - 1
            return len(ans)

        def bottomright(i, j):
            ans = set()
            i = i + 1
            j = j + 1
            while i < m and j < n:
                ans.add(grid[i][j]) 
                i = i + 1
                j = j + 1
            return len(ans)

        out = []
        for r in range(m):
            temp = []
            for c in range(n):
                tl = topleft(r,c)
                br = bottomright(r,c)
                temp.append(abs(tl-br))
            out.append(temp)
        return out
        
grid = [[1,2,3],[3,1,5],[3,2,1]]
ans = Solution().differenceOfDistinctValues(grid)
print(ans)
