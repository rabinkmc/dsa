from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int, used=set()) -> List[List[int]]:
        # print(
        #     k, n, f"{k} >= 1 and {n} <= 0 and {n} >= 10", k >= 1 and n <= 0 and n >= 10
        # )
        if k >= 1 and n <= 0 and n >= 10:
            return []
        if k == 1 and 1 <= n <= 9:
            if n not in used:
                return [[n]]
            return []
        answer = []
        for num in range(1, max(n, 10)):
            out = self.combinationSum3(k - 1, n - num, used)
            if out:
                result = [[num] + result for result in out]
                used.add(num)
                answer.extend(result)
        return answer


print(Solution().combinationSum3(2, 5))
