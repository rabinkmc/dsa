from typing import List
from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_q = deque()
        min_q = deque()
        left = 0
        n = len(nums)
        count = 0
        for right in range(n):
            while max_q and nums[max_q[-1]] < nums[right]:
                max_q.pop()
            max_q.append(right)
            while min_q and nums[min_q[-1]] > nums[right]:
                min_q.pop()
            min_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            count += right - left + 1
        return count

nums = [5, 4, 2, 4]
ans = Solution().continuousSubarrays(nums)
print(ans)
        
