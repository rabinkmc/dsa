from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        ans = 0
        tasks.sort(reverse=True)
        processorTime.sort()
        for i in range(0, len(processorTime)):
            new_time = processorTime[i] + max(tasks[4 * i : 4 * i + 4])
            ans = max(new_time, ans)
        return ans


processorTime = [8, 10]
tasks = [2, 2, 3, 1, 8, 7, 4, 5]
ans = Solution().minProcessingTime(processorTime, tasks)
print(ans)
