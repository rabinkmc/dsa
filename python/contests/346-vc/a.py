class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        prev = ""
        while i < len(s) and s != prev:
            if s[i:i+2] == "AB" or s[i:i+2] == "CD":
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i = i + 1
        return len(s)

s = "ACBBD"
s = Solution().minLength(s)
print(s)
