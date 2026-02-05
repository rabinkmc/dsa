from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_count = dict()
        t_count = dict()

        for ch in t:
            t_count[ch] = t_count.get(ch, 0) + 1

        for key in t_count:
            s_count[key] = 0

        i = 0
        j = 0
        n = len(s)
        ans = (-n, n)
        for j in range(n):
            ch = s[j]
            if ch in s_count:
                s_count[ch] += 1

            def check(c1, c2):
                for key in c2:
                    if c1.get(key, 0) < c2[key]:
                        return False
                return True

            while check(s_count, t_count):
                if ans[1] - ans[0] > j - i:
                    ans = (i, j)
                ch = s[i]
                if ch in s_count:
                    s_count[ch] -= 1
                i += 1

        if ans == (-n, n):
            return ""

        return s[ans[0] : ans[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"
ans = Solution().minWindow(s, t)
print(ans)
