from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_work = logs[0][1]
        ans = logs[0][0]
        for i in range(1, len(logs)):
            work_duration = logs[i][1] - logs[i - 1][1]
            case1 = (work_duration == max_work) and (logs[i][0] < ans)
            case2 = work_duration > max_work
            if case1 or case2:
                max_work = work_duration
                ans = logs[i][0]
        return ans


n = 10
logs = [[0, 3], [2, 5], [0, 9], [1, 15]]
ans = Solution().hardestWorker(n, logs)
print(ans)
