from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        items = sorted(zip(ages, scores))
        n = len(items)
        dp = [items[i][1] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if items[j][0] == items[i][0] or (items[j][1] <= items[i][1]):
                    dp[i] = max(dp[j] + items[i][1], dp[i])
        return max(dp)


#
#
# scores = [1, 3, 5, 10, 15]
# ages = [1, 2, 3, 4, 5]
scores = [4, 5, 6, 5]
ages = [2, 1, 2, 1]
ans = Solution().bestTeamScore(scores, ages)
print(ans)
