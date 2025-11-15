from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j]:
                    ans = 1
        # for row in dp:
        #     print(",".join(str(x) for x in row))
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] != 1:
                    continue
                a = dp[i - 1][j - 1]
                b = dp[i][j - 1]
                c = dp[i - 1][j]
                dp[i][j] = min(a, b, c) + 1
                ans = max(ans, dp[i][j])
        for row in dp:
            print(",".join(str(x) for x in row))
        return ans * ans


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
matrix = [["0", "0"], ["0", "0"]]
matrix = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1"],
]
ans = Solution().maximalSquare(matrix)
