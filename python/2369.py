from typing import List
from functools import lru_cache


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        def check2(i):
            if i + 1 >= n:
                return False
            return nums[i] == nums[i + 1]

        def check3(i):
            if i + 2 >= n:
                return False
            case1 = nums[i] == nums[i + 1] == nums[i + 2]
            case2 = (nums[i + 2] - nums[i + 1] == 1) and (nums[i + 1] - nums[i] == 1)
            return case1 or case2

        @lru_cache(None)
        def f(i):
            if i > n:
                return False
            if i == n:
                return True
            case1, case2 = False, False
            if check2(i):
                case1 = f(i + 2)
            if check3(i):
                case2 = f(i + 3)
            return case1 or case2

        return f(0)


nums = [1, 1, 1, 2, 2, 2, 2, 3, 6, 5]
ans = Solution().validPartition(nums)
print(ans)
