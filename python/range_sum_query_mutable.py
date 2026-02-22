from typing import List

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n  + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i +=  i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s


class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums
        n  = len(nums)
        self.ft = FenwickTree(n)
        for i in range(n):
            self.ft.update(i+1, nums[i])

    def update(self, index: int, val: int) -> None:
        self.ft.update(index + 1, val - self.arr[index])
        self.arr[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return self.ft.query(right + 1) - self.ft.query(left)
        


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
# param_2 = obj.sumRange(left,right)

