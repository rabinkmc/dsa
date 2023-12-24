from typing import List

from itertools import combinations

# I can use all numbers from 1 to 9 
n = 13


"""
13
(13-1) (13-2) (13 -3) (13-4) (13-5) ... .(13-9)

(12-2) - (12-3) - ...(12-9)

(10 - 3)

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        def dfs(i, path=[], total=0):
            if len(path) == k:
                if total == n:
                    answer.append(path)
                return 
            for j in range(i+1, 9+1):
                if total >n:
                    break
                dfs(j, path + [j], total + j)
        dfs(0)

        return answer
       


print(Solution().combinationSum3(3, 7))
