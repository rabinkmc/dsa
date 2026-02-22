from typing import List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.initial = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = list(self.initial)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(1, len(self.nums)):
            j = randint(0, i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


nums = [3, 1, 2]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
