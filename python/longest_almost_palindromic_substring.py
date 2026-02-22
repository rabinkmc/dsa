from functools import lru_cache

class Solution:
    def almostPalindromic(self, s: str) -> int:
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def f(l, r):
            while l < r:
                if s[l] != s[r]:
                    return check(l+1, r) or check(l, r-1)
                l, r = l + 1, r - 1
            return True
        n = len(s) 
        for length in range(n, 0, -1): 
            for start in range(n - length + 1):
                if f(start, start + length-1):
                    return length
        return 1

s = "zzabba"
ans = Solution().almostPalindromic(s)
print(ans)
