from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0 
        j = m * n - 1
        while i <= j:
            mid = ( i + j ) // 2
            r, c = mid // n,   mid % n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                i = mid + 1
            else:
                j = mid - 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
ans = Solution().searchMatrix(matrix, target)
print(ans)
