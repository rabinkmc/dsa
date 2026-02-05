from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        j = 0
        n = len(s)
        freq = dict()
        ans = 0
        counter = defaultdict(int)

        for j in range(minSize):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1

        ans = 0
        counter[s[: j + 1]] += 1

        if len(freq) <= maxLetters:
            ans += 1

        for j in range(minSize, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            preceding = s[j - minSize]
            freq[preceding] -= 1
            if freq[preceding] == 0:
                del freq[s[j - minSize]]

            if len(freq) <= maxLetters:
                substr = s[j - minSize + 1 : j + 1]
                counter[substr] += 1
                ans = max(ans, counter[substr])
        return ans


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
ans = Solution().maxFreq(s, maxLetters, minSize, maxSize)
print(ans)
