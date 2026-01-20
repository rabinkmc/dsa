from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answers = []
        candidates.sort()
        n = len(candidates)

        def dfs(i, total, subset):
            if total == 0:
                self.answers.append(subset)
                return

            if total < 0:
                return

            if i >= n:
                return
            dfs(i + 1, total - candidates[i], subset + [candidates[i]])
            j = i + 1
            while j < n and candidates[j] == candidates[j - 1]:
                j = j + 1
            dfs(j, total, subset)

        dfs(0, target, [])
        return self.answers


ans = Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8)
print(ans)
