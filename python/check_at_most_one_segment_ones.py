class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        pref = []
        curr = 0
        zero_seen = False
        for i in range(len(s)):
            if zero_seen and s[i] == "1":
                return False
            if s[i] == "0":
                zero_seen = True
        return True


s = "1001"
ans = Solution().checkOnesSegment(s)
print(ans)
