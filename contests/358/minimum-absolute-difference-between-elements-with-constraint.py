from typing import List
from heapq import heappush
import bisect
from sortedcontainers import SortedList


class Solution:
    """
    maintain a sorted list and search for the closest element to nums[i] 
    on the sorted list 
    """

    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums) 
        arr = SorteList()
        ans = float('inf')
        for i in range(x, n):
            """
            closest two elements are left and right
            so checking which one is the closest

            if we do our binary search left is always going to be higher than right 
            at terminating condition
            """
            idx = bisect.bisect_left(arr, nums[i])
            right, left = idx, idx - 1 
            def get_closest(arr, left, right):
                if right >= len(arr):
                    return arr[left]
                if  left < 0:
                    return arr[right]
                if abs(arr[left] - nums[i]) < abs(arr[right] - nums[i]):
                    return arr[left]
                else:
                    return arr[right]
            closest = get_closest(arr, left, right)
            ans = min(ans, abs(nums[i] - closest))
        return ans
            

nums = [32,129,93]
nums = [1, 74, 40, 99]
x = 1
ans = Solution().minAbsoluteDifference(nums, x)
assert ans == 25, ans

nums = [4,3,2,4]
x = 2
ans = Solution().minAbsoluteDifference(nums, x)
assert ans == 0, ans

nums = [5,3,2,10,15]
x = 1
ans = Solution().minAbsoluteDifference(nums, x)
assert ans == 1, ans

nums = [1,2,3,4]
x = 3
ans = Solution().minAbsoluteDifference(nums, x)
assert ans == 3

