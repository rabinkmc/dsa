from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = nums[0]
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res


nums = [3, 2, 1, 5, 6, 4]
k = 2
# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4

Solution().findKthLargest(nums, k)
