class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        ans = 1
        i = 0
        curr = 1
        j = 1
        while j < n:
            if j < n and ord(s[j]) - ord(s[j - 1]) == 1:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1
            j = j + 1
        return max(ans, curr)


s = "orcvscn"
ans = Solution().longestContinuousSubstring(s)
print(ans)
