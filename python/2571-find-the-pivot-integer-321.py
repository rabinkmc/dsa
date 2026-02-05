# https://leetcode.com/contest/weekly-contest-321/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        p_square = ( n*n + n) // 2
        p = pow(p_square, 0.5)
        return p

ans = Solution().pivotInteger(8)
print(ans)
            
        
