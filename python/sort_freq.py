from collections import Counter
from collections import deque


class Solution:
    def sortVowels(self, s: str) -> str:
        counter = dict()
        n = len(s)
        # count, index
        for i in range(n):
            ch = s[i]
            if ch not in counter:
                counter[ch] = [1, i]
            else:
                counter[ch][0] += 1
        items = list(counter.items())
        items.sort(key=lambda x: (x[1][0], -x[1][1]))
        out = deque()
        while items:
            key, (count, idx) = items.pop()
            if key in "aeiou":
                out.extend([key] * count)
        res = []
        for ch in s:
            if ch not in "aeiou":
                res.append(ch)
            else:
                res.append(out.popleft())

        return "".join(res)


s = "leetcode"
ans = Solution().sortVowels(s)
print(ans)
