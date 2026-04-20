from typing import List
from heapq import heappush, heappop


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # first pick the earliest task
        items = [(et, pt, i) for i, (et, pt) in enumerate(tasks)]
        items.sort()
        pq = []
        out = []
        idx = 0
        ct = 0
        n = len(tasks)
        while idx < n or pq:
            if not pq and ct <= items[idx][0]:
                ct = items[idx][0]

            while idx < n and ct >= items[idx][0]:
                _, p, orig_index = items[idx]
                heappush(pq, (p, orig_index))
                idx += 1

            pt, orig_index = heappop(pq)
            ct = ct + pt
            out.append(orig_index)
        return out


tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
ans = Solution().getOrder(tasks)
print(ans)
