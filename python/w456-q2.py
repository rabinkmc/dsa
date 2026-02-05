from typing import List
from functools import lru_cache
def f(a, b):
    m = len(a)
    n = len(b)
    x = min(m, n)
    i = 0
    while i < x:
        if a[i] == b[i]:
            i += 1
        else:
            break
    return i

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        res = []
        n = len(words)

        @lru_cache(None)
        def check(i):
            return f(words[i], words[i+1])
        
        L = []
        for i in range(n-1):
            L.append(check(i))
        print(L)

        prefix = [0]*n
        for i in range(n-1):
            prefix[i+1] = max(L[i], prefix[i])

        suffix = [0]*n
        for i in range(n-2, -1, -1):
            suffix[i] = max(L[i], suffix[i+1])
        res = [0]*n
        if n == 1:
            return res
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1, n-1):
            curr = 0
            curr = max(prefix[i-1], suffix[i+1])
            if i - 1 >= 0 and i + 1 <= n - 1:
                curr = max(curr, f(words[i-1], words[i+1]))
            res[i] = curr
        return res

words = ["jump","run","run","jump","run"]
# words = ["dog", "racer", "car"]
ans = Solution().longestCommonPrefix(words)
print(ans)
