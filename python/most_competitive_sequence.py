from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        to_remove = len(nums) - k
        for num in nums:
            while stack and stack[-1] > num and to_remove > 0:
                stack.pop()
                to_remove -= 1
            stack.append(num)
        return stack[:k]


nums = [3, 5, 2, 6]
k = 2
nums = [2, 4, 3, 3, 5, 4, 9, 6]
k = 4
ans = Solution().mostCompetitive(nums, k)
print(ans)
