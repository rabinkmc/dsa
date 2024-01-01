from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0 
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i = i + 1
            j = j + 1
        return i

solution = Solution()
g = [1,2,3]
s = [1,1]
ans = solution.findContentChildren(g = [1,2,3], s = [1,1])
assert ans == 1, ans
ans = solution.findContentChildren(g = [1,2], s = [1,2, 3])
assert ans == 2, ans
