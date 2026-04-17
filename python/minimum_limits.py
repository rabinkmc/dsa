from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def min_ops(num, x):
            rem = num % x
            parts = num // x
            if rem != 0:
                parts += 1
            return parts - 1

        def check(x):
            ops = 0
            for num in nums:
                if num <= x:
                    continue
                op = min_ops(num, x)
                ops += op
            return ops <= maxOperations

        l, r = 1, max(nums)
        ans = r
        while l <= r:
            m = l + (r - l) // 2
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


nums = [2, 4, 8, 2]
maxOperations = 4
nums = [9]
maxOperations = 2
ans = Solution().minimumSize(nums, maxOperations)
print(ans)
