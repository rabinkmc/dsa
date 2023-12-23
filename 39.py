from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answers = []
        self.sum_paths(candidates, target, self.answers)
        return self.answers

    def sum_paths(self, candidates, target, answers, path=[]):
        if target < 0:
            return
        if target == 0:
            answers.append(sorted(path))

        for num in candidates:
            if target - num < 0:
                return
            self.sum_paths(candidates, target - num, answers, path=[num, *path])


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
