from typing import List
from heapq import heappush, heappop, heapify


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idle_servers = [(wt, idx) for idx, wt in enumerate(servers)]
        heapify(idle_servers)
        busy_servers = []
        res = []
        for t, task in enumerate(tasks):
            idx = -1
            while busy_servers and busy_servers[0][0] <= t:
                _, wt, idx = heappop(busy_servers)
                heappush(idle_servers, (wt, idx))
            if idle_servers:
                wt, idx = heappop(idle_servers)
                heappush(busy_servers, (t + task, wt, idx))
            else:
                ctime, wt, idx = heappop(busy_servers)
                heappush(busy_servers, (ctime + task, wt, idx))
            res.append(idx)
        return res


servers = [3, 3, 2]
tasks = [1, 2, 3, 2, 1, 2]
ans = Solution().assignTasks(servers, tasks)
print(ans)
