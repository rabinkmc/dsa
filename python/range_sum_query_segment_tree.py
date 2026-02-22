from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, pos, start, end):
        if start == end:
            self.tree[pos] = nums[start]
            return
        mid = start + (end - start) // 2
        left = 2 * pos + 1
        right = 2 * pos + 2
        self.build(nums, left, start, mid)
        self.build(nums, right, mid+1, end)
        self.tree[pos] = self.tree[left] + self.tree[right]

    def update_tree(self, pos, start, end, idx, val):
        if start == end:
            self.tree[pos] = val
            return
        mid = (start + end) // 2
        left = 2* pos + 1
        right = 2 * pos + 2
        if idx <= mid:
            self.update_tree(left, start, mid, idx, val)
        else:
            self.update_tree(right, mid+1, end, idx, val)
        self.tree[pos] = self.tree[left] + self.tree[right]

    def update(self, index: int, val: int) -> None:
        self.update_tree(0, 0, self.n - 1, index, val)

    def query(self, pos, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[pos]
        mid = start + (end - start) // 2
        left = 2 * pos + 1
        right = 2 * pos + 2
        lsum = self.query(left, start, mid, l, r)
        rsum = self.query(right, mid+1,end, l, r)
        return lsum + rsum

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, 0, self.n - 1, left, right)

nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
