from typing import List


class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        graph = [list() for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)

        stack = []
        stack.append((0, cost[0]))
        parent = [-1] * n
        max_path_sum = 0
        leaf_nodes = []
        max_leaf = -1
        while stack:
            node, total = stack.pop()
            if not graph[node]:
                if total > max_path_sum:
                    max_path_sum = total
                    max_leaf = node
                leaf_nodes.append(node)
            for adj in graph[node]:
                parent[adj] = node
                stack.append((adj, total + cost[adj]))

        curr = max_leaf
        while curr != -1:
            print(curr)
            curr = parent[curr]


n = 3
edges = [[0, 1], [0, 2]]
cost = [2, 1, 3]
print(Solution().minIncrease(n, edges, cost))
