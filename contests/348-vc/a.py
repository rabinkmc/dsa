class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))  

s = "dddaaa"
print(Solution().minimizedStringLength(s))

