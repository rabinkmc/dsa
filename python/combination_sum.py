from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        ans = []
        candidates.sort()
        n = len(candidates)
        def backtrack(rem, start):
            if rem == 0:
                ans.append(curr[:])
                return
            for i in range(start, n):
                if candidates[i] > rem:
                    break
                curr.append(candidates[i])
                backtrack(rem - candidates[i], i)
                curr.pop()
        backtrack(target, 0)
        return ans

candidates = [2,3,6,7]
target = 7
ans = Solution().combinationSum(candidates, target)
print(ans)
