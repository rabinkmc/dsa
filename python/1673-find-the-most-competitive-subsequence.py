from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nk = n - k
        stack = []
        for i in range(n):
            while nk and stack and stack[-1] > nums[i]:
                stack.pop()
                nk -= 1
            stack.append(nums[i])

        return stack[:k]


nums = [3, 5, 2, 6]
nums = [2, 4, 3, 3, 5, 4, 9, 6]
k = 4
ans = Solution().mostCompetitive(nums, 4)
print(ans)
