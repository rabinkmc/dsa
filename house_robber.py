# https://leetcode.com/problems/house-robber/

# at each point i can either pick the current index maximum or the maximum of adjacent
from typing import List


class Solution:
    answers = dict()

    def rob(self, nums: List[int]) -> int:
        return self._rob(nums, len(nums) - 1)

    def _rob(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k in self.answers:
            return self.answers[k]
        self.answers[k] = max(nums[k] + self._rob(nums, k - 2), self._rob(nums, k - 1))
        return self.answers[k]


# nums = [1,2,3,1]
nums = [2, 7, 9, 3, 1]
answer = Solution()
print(answer.rob(nums))
