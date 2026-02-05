from typing import List
from collections import Counter

# brute force solution

# def next_candidates(candidates, candidate):
#     next_cand = []
#     append = next_cand.append
#     for next_candidate in candidates:
#         if abs(candidate - next_candidate) <= 1:
#             continue
#         append(next_candidate)
#     return next_cand


# def backtrack(candidates):
#     if not candidates:
#         return 0
#     ans = 0
#     for candidate in set(candidates):
#         next_cand = next_candidates(candidates, candidate)
#         current_sum = candidates.count(candidate) * candidate
#         earnings = current_sum + backtrack(next_cand)
#         ans = max(ans, earnings)
#     return ans


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        numbers = list(set(nums))
        numbers.sort()
        n = len(numbers)
        dp = [num * counter[num] for num in numbers]
        dp.append(0)
        for i in range(n - 2, -1, -1):
            if numbers[i] == numbers[i + 1] - 1:
                dp[i] = max(dp[i + 2] + dp[i], dp[i + 1])
            else:
                dp[i] = dp[i + 1] + dp[i]
        return dp[0]


nums = [2, 2, 3, 3, 3, 4]
nums = [1, 3]
print(Solution().deleteAndEarn(nums))
