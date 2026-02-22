from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        next_one = [-1] * n
        prev_one = [-1] * n
        curr = 0 if seats[0] == 1 else -1
        for i in range(1, n):
            if seats[i] == 0:
                prev_one[i] = curr
            else:
                curr = i
        curr = n-1 if seats[n-1] == 1 else -1
        for i in range(n-2, -1, -1):
            if seats[i] == 0:
                next_one[i] = curr;
            else:
                curr = i
        ans = 0
        for i in range(n):
            if seats[i] == 1:
                continue
            if prev_one[i] == -1:
                dist = next_one[i]
                ans = max(ans, next_one[i])
            elif next_one[i] == -1:
                dist = n - 1 - prev_one[i]
                ans = max(ans, n - 1 - prev_one[i])
            else:
                dist = (next_one[i] - prev_one[i])//2
                ans = max(ans, dist)
        return ans

seats = [1,0,0,0,1,0,1]
ans = Solution().maxDistToClosest(seats)
print(ans)
        
