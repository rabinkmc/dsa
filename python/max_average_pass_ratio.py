from typing import List
from heapq import heappush, heappop


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def f(p, t):
            avg = p / t
            new_avg = (p + 1) / (t + 1)
            return new_avg - avg

        pq = []
        for klass in classes:
            heappush(pq, [-f(klass[0], klass[1]), klass[0], klass[1]])
        for _ in range(extraStudents):
            _, np, nt = heappop(pq)
            heappush(pq, [-f(np + 1, nt + 1), np + 1, nt + 1])
        total = 0
        for item in pq:
            total += item[1] / item[2]
        return total / len(classes)


classes = [[1, 2], [3, 5], [2, 2]]
extraStudents = 2

classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
ans = Solution().maxAverageRatio(classes, extraStudents)
print(ans)
