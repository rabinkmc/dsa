class Solution:
    def minOperations(self, s: str) -> int:
        target = "".join(sorted(s))
        if s == target:
            return 0
        n = len(s)
        if n == 2:
            return -1

        def f1(s):
            return s[0] + "".join(sorted(s[1:]))

        def f2(s):
            return "".join(sorted(s[:-1])) + s[-1]

        if f1(s) == target or f2(s) == target:
            return 1
        
        if f1(f2(s)) == target or f2(f1(s)) == target:
            return 2
        return 3

s = "cba"
ans = Solution().minOperations(s)
print(ans)
        
