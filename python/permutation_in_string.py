class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        if n < k:
            return False
        k = len(s1)
        s1_sorted = sorted(s1)
        for i in range(n - k):
            if s1_sorted == sorted(s2[i : i + k]):
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
ans = Solution().checkInclusion(s1, s2)
print(ans)
