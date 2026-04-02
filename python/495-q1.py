class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                return l
            l, r = l + 1, r - 1
        return -1


s = "abcacbd"
s = "abc"
ans = Solution().firstMatchingIndex(s)
print(ans)
