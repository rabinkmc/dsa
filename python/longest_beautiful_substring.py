class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        idx = 0
        n = len(word)
        ans = 0
        curr = 1 if word[0] == "a" else 0
        for i in range(n):
            if word[i] not in vowels:
                continue
            if i > 0 and word[i] >= word[i - 1] and curr > 0:
                curr += 1
                if word[i] > word[i - 1]:
                    unique_vowels += 1
            elif word[i] == "a":
                curr = 1
                unique_vowels = 1
            else:
                curr = 0
                unique_vowels = 0
            if unique_vowels == 5:
                ans = max(ans, curr)
        return ans


word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
# word = "aeeeiiiioooauuuaeiou"
# word = "a"
ans = Solution().longestBeautifulSubstring(word)
print(ans)
