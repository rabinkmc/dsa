from typing import List
"""
1 12 3
4 15 6
7 8 9
"""

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        def find_min(start_row, start_col):
            numbers = set()
            for i in range(start_row, start_row + k):
                for j in range(start_col, start_col + k):
                    numbers.add(grid[i][j])
            if len(numbers) == 1:
                return 0
            arr = sorted(list(numbers))
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                diff = min(diff, abs(arr[i] - arr[i-1]))
            return diff
        ans = [[-1]*(n-k+1) for _ in range(m-k+1)]
        for i in range(m-k+1):
            for j in range(n-k+1):
                ans[i][j] = find_min(i, j)
        return ans

grid = [[1,-2,3],[2,3,5]]
k = 2
grid = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
grid = [[1, 8], [3, -2]]
ans = Solution().minAbsDiff(grid, k)
print(ans)
        
