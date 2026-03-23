from typing import List

class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        ws = []
        for word in words:
            if len(word) >= k:
                ws.append(word[:k])
        ws.sort()
        curr = 1
        ans = 0
        for i in range(1, len(ws)):
            if ws[i] == ws[i-1]:
                curr += 1
            else:
                if curr > 1:
                    ans += 1
                curr = 1
        if curr > 1:
            ans += 1
        return ans


words = ["apple","apply","banana","bandit"]
k = 2
# words = ["car","cat","cartoon"]
# k = 3
# words = ["bat","dog","dog","doggy","bat"]
# k = 3
print(Solution().prefixConnected(words, k))
