from collections import Counter


def isDigit(ch):
    return ch >= "0" and ch <= "9"


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        pairs = set()
        for ch in s:
            if ch in pairs:
                continue
            m = ""
            if isDigit(ch):
                m = str(9 - int(ch))
            else:
                cdist = ord(ch) - ord("a")
                m = chr(ord("z") - cdist)
            ans += abs(freq[ch] - freq[m])
            pairs.add(ch)
            pairs.add(m)
        return ans


s = "ab1z9"
s = "kk"
ans = Solution().mirrorFrequency(s)
print(ans)
