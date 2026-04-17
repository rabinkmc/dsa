class Solution:
    def countHomogenous(self, s: str) -> int:
        curr = 1
        ans = 0
        for j in range(1, len(s)):
            if s[j] == s[j - 1]:
                curr += 1
            else:
                ans += curr * (curr + 1) // 2
                curr = 1
        ans += curr * (curr + 1) // 2
        return ans


s = "abbcccaa"
ans = Solution().countHomogenous(s)
print(ans)
