from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(nums, candidates=[]):
            # if find_solution
            if len(candidates) == len(nums):
                answer.append(candidates)

            # get all possible candidats
            for num in nums:
                if num not in candidates:
                    backtrack(nums, candidates + [num])

        backtrack(nums)
        return answer


nums = [1, 2, 3]
ans = Solution().permute(nums)
assert ans == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
nums = [0, 1]
ans = Solution().permute(nums)
print(ans)
