class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(words[::-1])

ans = Solution().reverseWords("  the sky is blue  ")
print(ans)
        
