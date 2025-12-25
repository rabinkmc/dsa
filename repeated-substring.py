class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i != 0:
                continue
            substr = s[:i]
            k = n // i
            if substr * k == s:
                return True
        return False

s = "abcabcabcabc"
print()
ans = Solution().repeatedSubstringPattern(s)
print(ans)
        
