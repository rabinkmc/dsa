

# prefix[i] = sum of all numbers from 0 to i - 1
# so sum including index r  , prefix[r+1]
# so sum including range l, r, is 
# so sum(l, r) = p[r+1] - p[l]
def static_prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]

    def range_sum(l, r):
        return prefix[r+1] - prefix[l]
    return range_sum

# prefix sum is good for static arrays

# but if elements can change, prefix sum is too slow
# because each update would be 0(n)

# viable options
# 1. Fenwick Tree
# 2. Segment Tree

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.query(r) - self.query(l-1)

nums = [1, 3, 5, 7, 9]
n = len(nums)
ft = FenwickTree(n-1)

for i in range(1, n):
    ft.update(i, nums[i])
print(ft.range_sum(1, 3))
