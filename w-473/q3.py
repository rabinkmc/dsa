from typing import List

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        psum = [capacity[0]]
        for cap in capacity[1:]:
            psum.append(psum[-1] + cap)
        print(psum)
        return 0


ans = Solution().countStableSubarrays([9, 3, 3, 3, 9])
print(ans)
