from typing import List
from collections import defaultdict


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        words_map = defaultdict(list)
        for idx, word in enumerate(words):
            words_map[word].append(idx)
        if target not in words_map:
            return -1
        positions = words_map[target]
        ans = len(words)
        for pos in positions:
            cdist = abs(startIndex - pos)
            ans = min(ans, cdist, len(words) - cdist)
        return ans


words = ["hello", "i", "am", "leetcode", "hello"]
target = "hello"
startIndex = 1
words = ["a", "b", "leetcode"]
target = "leetcode"
startIndex = 0
ans = Solution().closestTarget(words, target, startIndex)
print(ans)
