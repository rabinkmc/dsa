class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        idx = p.index("*")
        p1 = p[:idx]
        p2 = p[idx + 1 :]
        left = s.find(p1)
        right = s.find(p2, left + len(p1))
        return left != -1 and right != -1


s = "leetcode"
p = "ee*e"
ans = Solution().hasMatch(s, p)
print(ans)
