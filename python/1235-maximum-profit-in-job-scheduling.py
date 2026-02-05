from typing import List
import bisect


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        """
        this problem can be modeled as finding the longest path in a dag 
        """
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        n = len(jobs)
        dp = [-1]*(n+1)
        starts = [job[0] for job in jobs]
        def dfs(i):
            if i == n:
                dp[i] = 0
                return 0
            if dp[i] != -1:
                return dp[i]
            next_i = bisect.bisect_left(starts, jobs[i][1])
            dp[i] = max(dfs(i+1), jobs[i][2] + dfs(next_i))
            return dp[i]
        return dfs(0)

startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]

startTime = [4,2,4,8,2]
endTime = [5,5,5,10,8]
profit = [1,2,8,10,4]

ans = Solution().jobScheduling(startTime, endTime, profit)
print(ans)
