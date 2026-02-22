from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            while max_q and nums[max_q[-1]] < val:
                max_q.pop()
            max_q.append(right)
            while min_q and nums[min_q[-1]] > val:
                min_q.pop()
            min_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            ans = max(ans, right - left + 1)
        return ans

nums = [8, 2, 4, 7]
ans = Solution().longestSubarray(nums, 4)
print(ans)
        
