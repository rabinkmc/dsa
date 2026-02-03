class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            val = ord(ch) - ord('A') + 1
            ans = ans * 26 + val
        return ans

ans = Solution().titleToNumber("ZY")
print(ans)
        
