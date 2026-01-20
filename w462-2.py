from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        prevs = [weight[0]]
        count = 0
        for i in range(1, n):
            if weight[i] < prevs[-1]:
                prevs.append(weight[i])
            else:
                count += len(prevs) // 2
                prevs = [weight[i]]
        count += len(prevs) // 2
        return count


weight = [2, 5, 1, 4, 3]
weight = [4, 4]
ans = Solution().maxBalancedShipments(weight)
print(ans)
