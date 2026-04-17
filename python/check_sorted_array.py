from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        dups = nums + nums[:-1]
        n = len(nums)
        arr = sorted(nums)
        for i in range(n):
            if dups[i : i + n] == arr:
                return True
        return False


nums = [3, 4, 5, 1, 2]
ans = Solution().check(nums)
print(ans)
