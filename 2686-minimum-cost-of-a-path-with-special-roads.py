# https://leetcode.com/contest/weekly-contest-343/problems/minimum-cost-of-a-path-with-special-roads/
from typing import List

from math import inf
from heapq import heappop, heappush


def mdist(s, e):
    x1, y1 = s
    x2, y2 = e
    return abs(x2 - x1) + abs(y2 - y1)


class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        source = start[0], start[1]
        end = target[0], target[1]

        def next_candidates(s1):
            end_edge = (end, mdist(s1, end))
            next_nodes = [end_edge]
            direct_dist = mdist(s1, target)
            for x1, y1, x2, y2, w in specialRoads:
                s2 = x1, y1
                e = x2, y2
                edge_weight = mdist(s1, s2) + w
                if edge_weight < direct_dist:
                    next_nodes.append((e, edge_weight))
            return next_nodes

        # initialize distances
        distances = dict()
        distances[source] = 0
        distances[end] = mdist(source, end)
        for road in specialRoads:
            node = (road[2], road[3])
            distances[node] = inf

        heap = [(source, 0)]
        while heap:
            node, curr_dist = heappop(heap)
            if curr_dist > distances[node]:
                continue
            for next_node, weight in next_candidates(node):
                dist = curr_dist + weight
                if dist < distances[next_node]:
                    distances[next_node] = dist
                    heappush(heap, (next_node, dist))
        return distances[end]


# start = [1, 1]
# target = [4, 5]
# specialRoads = [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]]

# ans = Solution().minimumCost(start, target, specialRoads)
print(
    Solution().minimumCost(
        start=[3, 2],
        target=[5, 7],
        specialRoads=[[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]],
    )
)

print(Solution().minimumCost([1, 1], [8, 3], [[2, 3, 8, 2, 3], [1, 1, 7, 3, 3]]))
