from typing import List
from collections import defaultdict

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


class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # degreee referes to the number of outgoing edges from the node
        n = len(graph)
        incoming_graph = [list() for _ in range(n)]
        degrees = [0]*n
        for node in range(n):
            degrees[node] = len(graph[node])
            for to_edge in graph[node]:
                incoming_graph[to_edge].append(node)

        queue = [node for node in range(n) if degrees[node] == 0]
        final_order = []
        # All the nodes whose outgoing degree is reduced to 0
        while queue:
            node = queue.pop()
            final_order.append(node)
            # now I have to find all the nodes whose outgoing edges connected to this particular node
            # and reduce thoses nodes degree by 1
            for next_node in incoming_graph[node]:
                degrees[next_node] -= 1
                if degrees[next_node] == 0:
                    queue.append(next_node)


        return sorted(final_order)


        
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution1().eventualSafeNodes(graph))
