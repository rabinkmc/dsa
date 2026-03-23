from typing import List

class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        for i, cap in enumerate(capacity):
            if cap < itemSize:
                continue
            if ans == -1:
                ans = i 
                continue
            if cap < capacity[ans]:
                ans = i
        return ans

        
