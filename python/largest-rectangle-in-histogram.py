from collections import deque
from typing import List


class MonotonicQueue:
    # increasing queue
    def __init__(self, heights):
        self.q = deque()
        self.heights = heights
        n = len(heights)
        for i in range(n):
            self.push(i)

    def push(self, i):
        while self.q and heights[self.q[-1]] >= heights[i]:
            self.q.pop()
        self.q.append(i)

    def pop(self, i):
        if i == self.top():
            self.q.popleft()

    def top(self):
        return self.q[0]


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        nse = [n] * n
        pse = [-1] * n

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        ans = 0
        for i in range(n):
            left = pse[i]
            right = nse[i]
            base = right - left - 1
            ans = max(ans, base * heights[i])
        return ans


heights = [2, 1, 5, 6, 2, 3]
heights = [1, 1]
ans = Solution().largestRectangleArea(heights)
print(ans)
