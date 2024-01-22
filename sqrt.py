class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x 
        left = 1
        right = x - 1
        ans = 0
        while left <= right:
            mid = left + (right - left)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1 
            else:
                ans = mid
                left = mid + 1
        return ans
            
            
x = 99
ans = Solution().mySqrt(x)
print(ans)
