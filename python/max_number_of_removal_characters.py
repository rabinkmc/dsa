from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        return 0


s = "abcacb"
p = "ab"
removable = [3, 1, 0]
ans = Solution().maximumRemovals(s, p, removable)
print(ans)
