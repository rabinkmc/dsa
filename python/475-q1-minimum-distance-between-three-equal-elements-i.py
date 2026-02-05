from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 101
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1, n):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j-k) + abs(k-i)
                        ans = min(ans, dist)
        if ans == 101:
            return -1
        return ans
