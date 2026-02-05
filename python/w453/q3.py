from typing import List
from collections import deque


class DecreasingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, num):
        while self.q and self.q[-1] < num:
            self.q.pop()
        self.q.append(num)

    def pop(self, num):
        if num == self.q[0]:
            self.q.popleft()


class IncreasingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, num):
        while self.q and self.q[-1] > num:
            self.q.pop()
        self.q.append(num)

    def pop(self, num):
        if num == self.q[0]:
            self.q.popleft()


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        cmax = nums[0]
        cmin = nums[0]
        total = 0
        inc_q = IncreasingQueue()
        dec_q = DecreasingQueue()
        for right in range(n):
            inc_q.push(nums[right])
            dec_q.push(nums[right])
            while (dec_q.q[0] - inc_q.q[0]) > k:
                inc_q.pop(nums[left])
                dec_q.pop(nums[left])
                left += 1
            total += right - left + 1
        return total


nums = [9, 4, 1, 3, 7]
k = 4
ans = Solution().countPartitions(nums, k)
print(ans)
