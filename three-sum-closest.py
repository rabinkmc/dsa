from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff = float("inf")
        ans = 0
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total

                cdiff = abs(total-target)
                if cdiff < diff:
                    diff = cdiff
                    ans = total

                if total > target:
                    k = k - 1
                else:
                    j = j + 1
        return ans
        
