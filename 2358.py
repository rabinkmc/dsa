from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        f = lambda x: x * (x + 1) // 2
        k = 1
        while f(k) and f(k+1) <= len(grades):
            k = k + 1

        return k

grades = [10,6,12,7,3,5, 4, 5, 5,5]
ans = Solution().maximumGroups(grades)
print(ans)
        
