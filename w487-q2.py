from typing import List
from collections import deque


class Solution:
    def finalElement(self, nums: List[int]) -> int:
        nums.sort()
        q = deque(nums)
        while len(q) > 1:
            if len(q) > 1:
                q.popleft()
            if len(q) > 1:
                q.pop()
        return q[0]


nums = [3, 7]
ans = Solution().finalElement(nums)
print(ans)
