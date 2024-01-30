from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        UNVISITED, VISITING, VISITED = 0, 1, 2
        n = len(graph)
        states = [UNVISITED]*n
        def has_cycle(node):
            if states[node] == VISITING:
                return True
            if states[node] == VISITED:
                return False
            states[node] = VISITING
            for next_node in graph[node]:
                if has_cycle(next_node):
                    return True
            states[node] = VISITED
            return False

        for node in range(n):
            if states[node] == UNVISITED:
                has_cycle(node)

        return [i for i in range(n) if states[i] == VISITED]
