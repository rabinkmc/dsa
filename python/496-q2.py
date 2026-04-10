import math


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        c = int(math.cbrt(n))
        counter = dict()
        out = []
        seen = set()
        for a in range(c + 1):
            for b in range(a + 1, c + 1):
                x = a * a * a + b * b * b
                if x > n:
                    continue
                if x in seen:
                    continue
                counter[x] = counter.get(x, 0) + 1
                if counter[x] >= 2:
                    seen.add(x)
                    out.append(x)
        out.sort()
        return out


n = 4104
ans = Solution().findGoodIntegers(n)
print(ans)
