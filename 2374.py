from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        incoming = [0]*n
        for i in range(n):
            node = edges[i]
            incoming[node] += i

        max_idx = 0
        for i in range(n):
            if incoming[i] > incoming[max_idx]:
                max_idx = i
        return max_idx

edges = [1,0,0,0,0,7,7,5]
ans = Solution().edgeScore(edges)
print(ans)
        
