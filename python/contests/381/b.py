from typing import List
def dist(h1, h2, x, y):
    d1 = abs(x-h1) + 1 + abs(y-h2)
    d2 = abs(h2 - h1)
    return min(d1, d2)



class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x, y = min(x, y), max(x,y)
        out = [0]*n
        for h1 in range(1,n+1):
            for h2 in range(h1+1, n+1):
                k = dist(h1, h2, x, y) - 1
                out[k] += 2
        return out

n, x, y = 5,2,4
ans = Solution().countOfPairs(n, x, y) 
print(ans)
