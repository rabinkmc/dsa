from typing import List
from collections import defaultdict
from functools import cache

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        counter = []
        running_counter = [0]*26


        for i in range(n):
            idx = ord('a') - ord(s[i])
            running_counter[idx] += 1 
            counter.append(running_counter.copy())

        @cache
        def check(i, j):
            """
            counter(i,j) = counter[j] - counter[i-1] for i > 0 
            otherwise
            counter[i][j]
            """
            state_j = counter[j]
            state_i = counter[i-1] if i > 0 else [0]*26 
            odd_state = 0
            for idx in range(26):
                count = state_j[idx] - state_i[idx]
                if count % 2 == 1:
                    odd_state += 1
            return odd_state // 2

        ans = []
        for i, j, k in queries:
            ans.append(k >= check(i, j))
        return ans

s = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
s = "lyb"
queries = [[0,1,0],[2,2,1]]
ans = Solution().canMakePaliQueries(s, queries)
print(ans)
