class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r):
            r = r - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        ans = s[0]
        max_length = 1
        for length in range(n, 0, -1):
            for start in range(n - length + 1):
                if check(start, start + length):
                    return s[start : start + length]
        return ans


print(Solution().longestPalindrome("babad"))
