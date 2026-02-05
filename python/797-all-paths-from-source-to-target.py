from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.answers = []
        n = len(graph)
        def dfs(i, subset):
            if i == n - 1:
                self.answers.append(subset)
                return 
            for next_node in graph[i]:
                dfs(next_node, subset + [next_node])
            return self.answers
        return dfs(0, [0])


graph = [[1, 2], [3], [3], []]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
ans = Solution().allPathsSourceTarget(graph)
print(ans)
