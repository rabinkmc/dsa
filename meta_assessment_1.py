class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        n = len(s)
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                vowels.append(s[i])
        out = []
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                out.append(vowels.pop())
            else:
                out.append(s[i])
        return "".join(out)


s = "IceCreAm"
ans = Solution().reverseVowels(s)
print(ans)
