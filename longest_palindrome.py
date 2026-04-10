class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def check(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for length in range(n, 0, -1):
            for i in range(n - length + 1):
                j = i + length - 1
                if check(i, j):
                    return s[i : j + 1]
        return ""


ans = Solution().longestPalindrome("babad")
print(ans)
