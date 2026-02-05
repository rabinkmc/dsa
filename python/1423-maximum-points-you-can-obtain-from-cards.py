from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints[n - k :])
        ans = total

        i = 0
        j = n - k

        for i in range(k):
            total = total - cardPoints[j % n] + cardPoints[i]
            j = j + 1
            ans = max(ans, total)
        return ans


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
ans = Solution().maxScore(cardPoints, k)
print(ans)
