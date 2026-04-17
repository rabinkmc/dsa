from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        # key observation is there are only two numbers that appear once. They are the ends
        # now stick to one end and reach till the end, and construct result
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        ends = []
        for node in graph:
            if len(graph[node]) == 1:
                ends.append(node)
        curr = ends[0]
        res = []
        seen = set()
        seen.add(curr)
        while curr != ends[1]:
            res.append(curr)
            next_nodes = graph[curr]
            if len(next_nodes) == 1:
                curr = next_nodes[0]
            else:
                if next_nodes[0] not in seen:
                    curr = next_nodes[0]
                else:
                    curr = next_nodes[1]
            seen.add(curr)
        res.append(ends[1])
        return res


adjacentPairs = [[2, 1], [3, 4], [3, 2]]
adjacentPairs = [[4, -2], [1, 4], [-3, 1]]
ans = Solution().restoreArray(adjacentPairs)
print(ans)
