from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res


temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
ans = Solution().dailyTemperatures(temperatures)
print(ans)
