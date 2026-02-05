from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (x1, x2), value in zip(equations, values):
            graph[x2][x1] = 1 / value
            graph[x1][x2] = value

        def dfs(node, end, visited, product=1):
            if node == end:
                return product
            visited.add(node)
            for next in graph[node]:
                weight = graph[node][next]
                if next in visited:
                    continue
                answer = dfs(next, end, visited, product * weight)
                if answer != -1:
                    return answer
            return -1

        answer = []
        for a, b in queries:
            if a not in graph or b not in graph:
                prod = -1
                answer.append(prod)
            else:
                prod = dfs(node=a, end=b, visited=set())
                answer.append(prod)
        return answer


equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
values = [3.0, 4.0, 5.0, 6.0]
queries = [
    ["x1", "x5"],
    ["x5", "x2"],
    ["x2", "x4"],
    ["x2", "x2"],
    ["x2", "x9"],
    ["x9", "x9"],
]

print(Solution().calcEquation(equations, values, queries))
