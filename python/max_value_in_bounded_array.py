class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum

        def check(x):
            if x == 1:
                return n <= maxSum

            if x > index:
                ls, le = x - index, x - 1
                lsum = ((ls + le) * (le - ls + 1)) // 2
            else:
                ls, le = 1, x - 1
                lsum = ((ls + le) * (le - ls + 1)) // 2 + (index - (x - 1))

            if x > (n - 1) - index:
                rs, re = x - (n - 1 - index), x - 1
                rsum = ((rs + re) * (re - rs + 1)) // 2
            else:
                rs, re = 1, x - 1
                rsum = (rs + re) * (re - rs + 1) // 2 + (n - 1 - index - (x - 1))
            if index == 0:
                lsum = 0
            if index == n - 1:
                rsum = 0
            return lsum + rsum + x <= maxSum

        ans = 0
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans


n = 4
index = 2
maxSum = 6

n = 6
index = 1
maxSum = 10
n = 1000000000
index = 100000000
maxSum = 1000000000
ans = Solution().maxValue(n, index, maxSum)
print(ans)
