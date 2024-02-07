from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2 * 1000_000_000

        def f(k):
            ab = (a*b) // gcd(a, b)
            bc = (b*c) // gcd(b, c)
            ac = (a*c) // gcd(a, c)
            abc =(ab * c) // gcd(ab, c) 
            return (k//a + k//b + k//c - k//(ab) - k//(bc) - k//(ac) + k//(abc))
        
        ans = -1
        while left <= right:
            m = left + (right - left)//2
            if f(m) >= n:
                ans = m 
                right = m - 1
            else:
                left = m + 1
        return ans
            
        
