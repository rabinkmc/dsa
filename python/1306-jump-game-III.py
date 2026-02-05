from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def neighbors(node):
            i1 = node + arr[node]
            i2 = node - arr[node]
            nodes = []
            if i1 < n:
                nodes.append(i1)
            if i2 >= 0:
                nodes.append(i2)
            return nodes

        queue = deque()
        queue.append(start)
        visited = {start}
        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True
            for next_node in neighbors(node):
                if next_node in visited:
                    continue
                queue.append(next_node)
                visited.add(next_node)
        return False



print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5))
        
