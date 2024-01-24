from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        # find the next candidates
        def next_candidate(i, res):
            set_i = set(res)
            candidates = []
            for j in range(i+1, n):
                set_j = set(arr[j])
                if len(arr[j]) != len(set_j):
                    continue
                if not (set_i & set_j):
                    candidates.append(j)
            return candidates

        self.answer = 0
        def dfs(i, res):
            candidates = next_candidate(i, res)
            if not candidates: 
                self.answer = max(self.answer, len(res))
                return

            for candidate in candidates:
                dfs(candidate, res + arr[candidate]) 

        # starting backtracking on all the possible starting nodes
        for i in range(n):
            if len(arr[i]) == len(set(arr[i])):
                dfs(i, arr[i])
        return self.answer

arr = ["un","iq","ue"]
arr = ["aa", "bb"]
ans = Solution().maxLength(arr)
print(ans)
