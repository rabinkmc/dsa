from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        curr = []
        self.ans = 0
        n = len(nums)

        def subsets(i, curr):
            if i == n:
                self.ans += curr
                return

            subsets(i + 1, curr ^ nums[i])
            subsets(i + 1, curr)

        subsets(0, 0)
        return self.ans


nums = [1, 3]
nums = [5, 1, 6]
ans = Solution().subsetXORSum(nums)
print(ans)
