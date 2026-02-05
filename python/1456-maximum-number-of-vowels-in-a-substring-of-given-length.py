class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = len(s)
        vowels = "aeiou"
        curr = 0
        ans = 0
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr

        for j in range(k, n):
            if s[j - k] in vowels:
                curr = curr - 1
            if s[j] in vowels:
                curr = curr + 1
            ans = max(ans, curr)

        return ans


s = "abciiidef"
k = 3

print()
print(Solution().maxVowels(s, k))
