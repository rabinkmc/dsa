from typing import List

def countBits(x):
    total = 0
    while x:
        total += x % 2
        x = x // 2
    return total

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        out = []
        for x in arr:
            out.append((countBits(x), x))
        return [x[1] for x in sorted(out)]

arr = list(range(9))
ans = Solution().sortByBits(arr)
print(ans)
        
