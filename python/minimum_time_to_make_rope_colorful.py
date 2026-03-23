from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        out = []
        ccount = 1
        cmax = neededTime[0]
        csum = neededTime[0]
        ans = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                ## time to remove
                ccount += 1
                cmax = max(cmax, neededTime[i])
                csum += neededTime[i]
            else:
                if ccount > 1:
                    ans += csum - cmax
                csum = neededTime[i]
                cmax = neededTime[i]
        if ccount > 1:
            ans += csum - cmax
        return ans


colors = "aabaa"
neededTime = [1, 2, 3, 4, 1]
ans = Solution().minCost(colors, neededTime)
print(ans)
