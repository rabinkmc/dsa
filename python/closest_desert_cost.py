from typing import List


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        n = len(toppingCosts)
        self.ans = float("inf")
        self.diff = float("inf")
        m = len(baseCosts)

        def f(i, cost):
            if i == n:
                for i in range(m):
                    diff = abs(cost + baseCosts[i] - target)
                    if diff < self.diff or (
                        diff == self.diff and cost + baseCosts[i] < self.ans
                    ):
                        self.ans = cost + baseCosts[i]
                        self.diff = diff
                return
            f(i + 1, cost)
            f(i + 1, cost + toppingCosts[i])
            f(i + 1, cost + toppingCosts[i] * 2)

        f(0, 0)
        return self.ans  # type: ignore


baseCosts = [1, 7]
toppingCosts = [3, 4]
target = 10
ans = Solution().closestCost(baseCosts, toppingCosts, target)
print(ans)
