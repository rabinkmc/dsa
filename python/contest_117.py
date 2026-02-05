from typing import List


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for i in range(limit + 1):
            target = n - i
            answer += self.twoSum(limit, target)
        return answer

    def twoSum(self, limit, target) -> int:
        answer = 0
        i = 0
        j = limit
        while i <= j:
            if i + j > target:
                j -= 1
            elif i + j < target:
                i += 1
            elif i + j == target:
                if i == j:
                    answer += 1
                else:
                    answer += 2
                i += 1
                j -= 1
        return answer


print(Solution().distributeCandies(5, 2))
