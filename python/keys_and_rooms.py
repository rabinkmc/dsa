from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        queue.append(0)
        n = len(rooms)
        visited = [False for _ in range(n)]
        count = 1
        visited[0] = True
        while queue:
            node = queue.popleft()
            for adj in rooms[node]:
                if visited[adj]:
                    continue
                visited[adj] = True
                count = count + 1
                queue.append(adj)
        return count == n

rooms = [[1,3],[3,0,1],[2],[0]]
ans = Solution().canVisitAllRooms(rooms)
print(ans)
                


        

        
