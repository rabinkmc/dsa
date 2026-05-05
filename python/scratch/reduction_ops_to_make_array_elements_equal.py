from typing import List
from collections import Counter


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        distinct = list(counter.keys())
        distinct.sort()
        if len(distinct) == 1:
            return 0
        n = len(distinct)
        ops = 0
        for i in range(1, n):
            ops += counter[distinct[i]] * i
        return ops


nums = [5, 1, 3]
nums = [1, 1, 1]
ans = Solution().reductionOperations(nums)
print(ans)
