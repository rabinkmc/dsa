from typing import List
from collections import defaultdict, Counter


def check_bits(n):
    while n:
        rem = n % 2
        n = n // 2
        if rem == 0:
            return False
    return True


class Solution:
    def countMonobit(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        ans = 2
        for i in range(2, n + 1):
            ans += int(check_bits(i))

        return ans


ans = Solution().countMonobit(15)
print(ans)
