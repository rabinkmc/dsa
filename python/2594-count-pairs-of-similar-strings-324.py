# https://leetcode.com/contest/weekly-contest-324/problems/count-pairs-of-similar-strings/
from typing import List
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)

        def check_pair(w1, w2):
            return set(w1) == set(w2)

        total = 0
        for i in range(n):
            for j in range(i+1, n):
                total += int(check_pair(words[i], words[j]))
        return total

words = ["aabb","ab","ba"]
words = ["aba","aabb","abcd","bac","aabc"]
ans = Solution().similarPairs(words)
print(ans)
        
