# https://leetcode.com/contest/weekly-contest-324/problems/add-edges-to-make-degrees-of-all-nodes-even/
from typing import List
from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)

        odd_nodes = []
        for node in graph:
            if len(graph[node]) % 2 == 1:
                odd_nodes.append(node)

        if len(odd_nodes) == 0:
            return True

        def f(a, b):
            return a not in graph[b]

        if len(odd_nodes) == 2:
            a, b = odd_nodes
            return any(f(a,i) and f(b,i) for i in range(n))

        if len(odd_nodes) == 4:
            a,b,c, d = odd_nodes
            return (
                (f(a,b) and f(c, d)) or
                (f(a,c) and f(b, d)) or
                (f(a,d) and f(b,c))
            )

        return False

n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
# n = 4
# edges = [[1,2],[3,4]]
# n = 4
# edges = [[1,2],[1,3],[1,4]]

n, edges = 4, [[6,4],[1,4],[1,6],[5,6]]
ans = Solution().isPossible(n, edges)
print(ans)

