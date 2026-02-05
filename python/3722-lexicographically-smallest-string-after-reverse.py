class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        ans = min(s, s[::-1])

        for i in range(2, n):
            front = s[:i][::-1] + s[i:]
            ans = min(ans, front)
            back = s[: n - i] + s[n - i :][::-1]
            ans = min(ans, back)

        return ans


print(Solution().lexSmallest("abba"))
