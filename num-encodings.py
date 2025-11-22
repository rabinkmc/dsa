class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dp(i):
            if i < n and s[i] == "0":
                return 0
            if i >= n - 1:
                return 1
            answer = dp(i + 1)
            ch = int(s[i : i + 2])
            if 10 <= ch <= 26:
                answer += dp(i + 2)
            return answer

        return dp(0)


print(Solution().numDecodings("231220"))
