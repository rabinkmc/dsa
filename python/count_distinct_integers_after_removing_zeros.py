class Solution:
    def countDistinct(self, n: int) -> int:
        def digits(x):
            rv = 0
            while x > 0:
                rv += 1
                x = x // 10
            return rv

        ans = 0
        p = digits(x)
        if p > 1:
            ans += 9 ** (p)
        for 

        return 0
