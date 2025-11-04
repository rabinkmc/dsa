from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ## idea is to have indegrees
        indegrees = [0 for _ in range(n)]
        for u, v in edges:
            indegrees[v] += 1
        ans = []
        for index, deg in enumerate(indegrees):
            if deg == 0:
                ans.append(index)
        return ans


edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
print(Solution().findSmallestSetOfVertices(6, edges))
