from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        visited = set()
        i = 0
        state = k 
        while i not in visited:
            visited.add(i)
            i = (i + state) % n
            state += k
        ans = []
        for i in range(n):
            if i not in visited:
                ans.append(i+1)
        return ans

ans = Solution().circularGameLosers(n = 5, k = 2)
print(ans)
        
