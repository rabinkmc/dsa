from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = [0] * 26
        for word in words:
            for ch in word:
                idx = ord(ch) - ord("a")
                counter[idx] += 1
        n = len(words)
        for count in counter:
            if count % n != 0:
                return False
        return True


words = ["abc", "aabc", "bc"]
ans = Solution().makeEqual(words)
print(ans)
