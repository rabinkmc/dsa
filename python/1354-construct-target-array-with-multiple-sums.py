from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1
        total = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)
        while -target[0] > 1:
            largest = -target[0]
            rest = total - largest

            if rest == 1:
                return True

            new = largest % rest
            if new == 0 or new == largest:
                return False
            heapq.heapreplace(target, -new)
            total = total - largest + new
        return True


target = [8, 5]
print(Solution().isPossible(target))
