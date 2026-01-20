from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        count = 0
        while amount[0] or amount[1] or amount[2]:
            amount.sort()
            count += 1
            amount[1] = max(0, amount[1] - 1)
            amount[2] = max(0, amount[2] - 1)

        return count

ans = Solution().fillCups(amount=[1, 4, 2])
