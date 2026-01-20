from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def f(num):
            res = 0
            while num:
                res += num % 10
                num = num // 10
            return res

        n = len(nums)
        idx_map = dict()
        for i in range(n):
            idx_map[nums[i]] = i
        sorted_nums = sorted(nums, key=lambda x: (f(x), x))
        swaps = 0
        for i in range(n):
            if nums[i] != sorted_nums[i]:
                j = idx_map[sorted_nums[i]]
                swaps += 1
                nums[i], nums[j] = nums[j], nums[i]
                idx_map[nums[i]], idx_map[nums[j]] = idx_map[nums[j]], idx_map[nums[i]]
        return swaps


nums = [1, 5, 3, 4, 2, 0]
ans = Solution().minSwaps(nums)
print(ans)
