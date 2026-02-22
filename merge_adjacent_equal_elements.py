from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for x in nums:
            prev = x
            while stack and stack[-1] == prev:
                stack.pop()
                prev = prev * 2
            stack.append(prev)
        return stack

nums = [2, 1, 1, 2]
ans =  Solution().mergeAdjacent(nums)
print(ans)
