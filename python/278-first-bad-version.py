# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        ans = 0
        while left <= right:
            m = (left + right)//2
            if isBadVersion(m):
                ans = m 
                right = m - 1
            else:
                left = m + 1
        return ans
        
