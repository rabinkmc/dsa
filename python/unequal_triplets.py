from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n - 2):
                    case1 = nums[i] != nums[j]
                    case2 = nums[j] != nums[k]
                    case3 = nums[k] != nums[i]
                    ans += int(case1 and case2 and case3)
        return ans
