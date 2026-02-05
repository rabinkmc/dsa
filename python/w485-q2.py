from typing import List
from collections import defaultdict, Counter
from itertools import permutations


class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        items = [(cost, cap) for (cost, cap) in zip(costs, capacity) if cost < budget]
        if len(items) == 0:
            return 0
        l = 0
        r = len(items) - 1
        items.sort()
        one_max = 0
        for item in items:
            one_max = max(one_max, item[1])
        ans = 0
        while l < r:
            if items[l][0] + items[r][0] < budget:
                ans = max(ans, items[l][1] + items[r][1])
                l += 1
            else:
                r -= 1
        if ans == 0:
            return one_max
        return ans


costs = [4, 8, 5, 3]
capacity = [1, 5, 2, 7]
budget = 8
costs = [3, 5, 7, 4]
capacity = [2, 4, 3, 6]
budget = 7
costs = [2, 2, 2]
capacity = [3, 5, 4]
budget = 5
costs = [4, 6]
capacity = [5, 3]
budget = 3
ans = Solution().maxCapacity(costs, capacity, budget)
print(ans)
