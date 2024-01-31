from typing import List
from collections import deque, defaultdict


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        graph = defaultdict(list)
        START = -1
        for emp, mgr in enumerate(manager):
            if mgr == -1:
                START = emp
                continue
            graph[mgr].append(emp)

        queue = deque()
        queue.append((START, 0))
        ans = 0
        while queue:
            node, time = queue.popleft()
            ans = max(ans, time)

            for next_node in graph[node]:
                queue.append((next_node, time + informTime[node]))
        return ans


ans = Solution().numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0])
# ans = Solution().numOfMinutes(n=1, headID=0, manager=[-1], informTime=[0])
print(ans)
