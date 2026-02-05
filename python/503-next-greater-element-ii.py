from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])

        peaks = [0] * n
        peaks[0] = nums[0]
        for i in range(1, n):
            peaks[i] = max(nums[i], peaks[i - 1])

        for i in range(n):
            if res[i] == -1:
                if i == 0:
                    continue
                peak = max(peaks[: i - 1])
                res[i] = peak if peak > nums[i] else -1
        return res


nums = [5, 2, 3, 4, 3]
ans = Solution().nextGreaterElements(nums)
print(ans)
