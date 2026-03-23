from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            do_nothing = dp[i + 1]
            point, skip = questions[i]
            solve = point + dp[min(n, i + skip + 1)]
            dp[i] = max(do_nothing, solve)
        return dp[0]


questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
ans = Solution().mostPoints(questions)
print(ans)
