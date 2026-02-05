from collections import Counter


class Solution:
    def balancedString(self, s):
        count = Counter(s)
        n = len(s)
        res = n
        i = 0
        for j, ch in enumerate(s):
            count[ch] -= 1
            while i < n and all(n / 4 >= count[ch] for ch in "QWER"):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i = i + 1
        return res


s = "QQQR"
print(Solution().balancedString(s))
