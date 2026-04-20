class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        out = s.strip().split()
        return " ".join(out[:k])


s = "Hello how are you Contestant"
k = 4
ans = Solution().truncateSentence(s, k)
print(ans)
