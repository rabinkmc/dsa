from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = []
        for i in range(1<<n): 
            ans.append(start ^ i ^ (i >> 1))
        return ans 

ans = Solution().circularPermutation(n=3, start=0)
print(ans)
