from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.psum = [0] * (n + 1)
        for i in range(n):
            self.psum[i + 1] = self.psum[i] + nums[i]
        print(self.psum)

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right + 1] - self.psum[left]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
left, right = 0, 2
print(obj.sumRange(left, right))
# param_1 = obj.sumRange(left,right)
