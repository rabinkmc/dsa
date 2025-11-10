class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        i = 0 
        j = 0
        n = len(s)
        ans = 0
        while (j < n):
            if (j - i + 1) < k:
                j += 1 
            else:
                a , b , c = s[i], s[i+1], s[i+2]
                if (a != b and a != c and b != c):
                    ans += 1
                i += 1
                j += 1
        return ans

print(Solution().countGoodSubstrings("xyzzaz"))
        
