from functools import lru_cache
from collections import Counter

@lru_cache(None)
def f(n):
    if n <= 1:
        return 1
    return f(n-1) * n

class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        total = 0
        x = n
        digits = []
        while x:
            digit = x % 10
            digits.append(str(digit))
            total += f(digit)
            x = x // 10
        new_digits = list(str(total))
        return Counter(new_digits) == Counter(digits)

n = 10
ans = Solution().isDigitorialPermutation(n)
print(ans)
