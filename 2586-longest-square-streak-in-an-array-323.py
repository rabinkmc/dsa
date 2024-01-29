# https://leetcode.com/contest/weekly-contest-323/problems/longest-square-streak-in-an-array/
from typing import List
import bisect 

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        numbers = [[1, num] for num in nums]
        n = len(numbers)

        def index(target):
            ip = bisect.bisect_left(nums, target)
            if ip != n  and nums[ip] == num * num:
                return ip
            return -1

        for idx, num in enumerate(nums):
            count = numbers[idx][0]
            ip = bisect.bisect_left(nums, num * num)
            if index(num * num) != -1:
                numbers[ip][0] = count + 1
        ans = max(numbers)[0]
        if ans == 1:
            return -1
        return ans

nums = [2, 4, 8, 16]
ans = Solution().longestSquareStreak(nums)
print(ans)
