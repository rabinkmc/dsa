from typing import List
from collections import deque


class MonotonicQueue:
    def __init__(self):
        self.q = deque()

    def push(self, n):
        while self.q and self.q[-1] < n:
            self.q.pop()
        self.q.append(n)

    def max(self):
        return self.q[0]

    def pop(self, n):
        if n == self.q[0]:
            self.q.popleft()


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        # push first k elements of the window
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        res.append(nums[q[0]])
        n = len(nums)
        for i in range(k, n):
            # pop the leftmost element
            if q[0] < i - k:
                q.popleft()

            # push the new element
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            # update the max of the window
            res.append(nums[q[0]])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k=3))
