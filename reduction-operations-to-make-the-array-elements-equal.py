from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        numbers = sorted(set(nums))
        operations = {}
        n = len(numbers)
        operations[numbers[0]] = 0
        for i in range(1, n):
            operations[numbers[i]] = i
        ans = 0
        for num in nums:
            ans += operations[num]
        return ans


nums = [1, 1, 2, 2, 3]
ans = Solution().reductionOperations(nums)
print(ans)
