from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(s):
            slist = [[s[0], 1]]
            for i in range(1, len(s)):
                if s[i] != s[i-1]:
                    slist.append([s[i], 1])
                else:
                    slist[-1][1] += 1
            return slist
        s_count = f(s)
        print(s_count)
        ans = 0
        for word in words:
            w_count = f(word)
            nw = len(w_count)
            if nw != len(s_count):
                continue
            state = True
            for i in range(nw):
                if s_count[i] == w_count[i]:
                    continue
                case1 = s_count[i][0] != w_count[i][0]
                case2 = s_count[i][1] < w_count[i][1]
                case3  = s_count[i][1] <= 2 and w_count[i][1] <= 1
                if case1 or case2 or case3:
                    state = False
                    break
            if state:
                ans += 1
        return ans

s = "heeellooo"
words = ["hello", "hi", "helo"]
words = ["hello"]
ans = Solution().expressiveWords(s, words)
print(ans)
