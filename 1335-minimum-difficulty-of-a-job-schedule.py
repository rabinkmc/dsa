from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        self.hardest = [-1] * n
        self.hardest[n - 1] = jobDifficulty[n - 1]
        for i in range(n - 2, -1, -1):
            self.hardest[i] = max(self.hardest[i + 1], jobDifficulty[i])

        memo = {}

        def dp(i, days):
            if days == d:
                return self.hardest[i]
            if (i, days) in memo:
                return memo[(i, days)]
            best = 1000000
            hardest = -1
            for j in range(i, n - (d - days)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, days + 1))
            memo[(i, days)] = best
            return best

        return dp(0, 1)


jobDifficulty = [6, 5, 4, 3, 10, 2, 1]
d = 3
print(Solution().minDifficulty(jobDifficulty, 2))
