from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(x) for x in accounts)


accounts = [[1, 2, 3], [3, 2, 1]]
ans = Solution().maximumWealth(accounts)
print(ans)
