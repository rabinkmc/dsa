from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def f(x):
            total = 0
            while x:
                total += (x % 10)
                x = x // 10
            return total
        map = defaultdict(list)
        for x in nums:
            map[f(x)].append(x)

        ans = -1
        for items in map.values():
            if len(items) > 1:
                items.sort()
                ans = max(ans,items[-1] + items[-2])
        return ans


nums = [18, 43, 36, 13, 7]
ans = Solution().maximumSum(nums)
print(ans)
        
