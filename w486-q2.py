from typing import List
from collections import deque

class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        arr = deque()
        idx = []
        for i, num in enumerate(nums):
            if num >= 0:
                arr.append(num)
                idx.append(i)

        n = len(arr)
        if n == 0:
            return nums

        k = k % n
        for i in range(k):
            arr.append(arr.popleft())

        for i, val in zip(idx, arr):
            nums[i] = val
        return nums

nums = [1, -2, 3, -4]
k = 3
nums = [-3, -2, 7]
k = 1
nums = [5,4,-9,6]
k = 2
nums = [-6, -2]
k = 18866
ans = Solution().rotateElements(nums, k)
print(ans)

