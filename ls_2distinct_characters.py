class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = dict()
        n = len(s)
        i = 0
        ans = 0
        for j in range(n):
            counter[s[j]] = counter.get(s[j], 0) + 1
            while len(counter) > 2:
                x = s[i]
                counter[x] -= 1
                if counter[x] == 0:
                    del counter[x]
                i = i + 1
            ans = max(ans, j - i + 1)
        return ans
