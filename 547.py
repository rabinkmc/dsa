from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def get_graph(isConnected):
            graph = {}
            for i, node in enumerate(isConnected):
                graph[i + 1] = []
                for j, connected in enumerate(node):
                    if i == j or not connected:
                        continue
                    graph[i + 1].append(j + 1)
            return graph

        graph = get_graph(isConnected)
        count = 0
        visited = set()
        for node in graph:
            if node in visited:
                continue
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                stack.extend(graph[cur])
            count += 1
            visited.add(node)

        return count


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(Solution().findCircleNum(isConnected))
