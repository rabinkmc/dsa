import heapq
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        pq = []
        total = 0
        for i in range(n):
            heapq.heappush(pq, -nums[i])
            if nums[i] == "1":
                total += -heappop(pq)
        return total


nums = [2, 1, 5, 2, 3]
s = "01010"
ans = Solution().maximumScore(nums, s)
