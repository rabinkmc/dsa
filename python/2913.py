from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                count = len(set(nums[i : j + 1]))
                answer += count**2
        return answer


answer = Solution().sumCounts([1, 1])
print(answer)
