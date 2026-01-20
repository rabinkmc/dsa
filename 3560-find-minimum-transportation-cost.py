class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost_m, cost_n = 0, 0
        if n > k:
            nl1, nl2 = n - k, k
            cost_n = nl1 * nl2

        if m > k:
            ml1, ml2 = n - k, k
            cost_n = ml1 * ml2
        return cost_m + cost_n
        
n = 6
m = 5
k = 5
ans = Solution().minCuttingCost(n, m, k)
