class Solution:
    def minSwaps(self, s: str) -> int:
        zeros = s.count("0")
        ones = s.count("1")
        if abs(zeros - ones) > 1:
            return -1
        n = len(s)
        # assume start = 0
        # assume start = 1
        curr = 0

        def f(curr):
            rv = 0
            for i in range(0, n, 2):
                if s[i] != curr:
                    rv += 1
            return rv

        if n % 2 == 0:
            return min(f("0"), f("1"))
        if zeros > ones:
            return f("0")
        return f("1")


s = "111000"
s = "010110"
ans = Solution().minSwaps(s)
print(ans)
