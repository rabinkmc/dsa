class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        count = 0
        res = []
        csum = 0
        for count in range(1, n + 1):
            for i in range(1, 27):
                rem = k - (csum + i)
                if rem <= 26 * (n - count):
                    res.append(i)
                    csum = csum + i
                    break
        out = []
        for ch in res:
            out.append(chr(ord("a") + (ch - 1)))
        return "".join(out)


n, k = 3, 27
ans = Solution().getSmallestString(n, k)
print(ans)
