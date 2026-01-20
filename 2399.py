from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = 26
        map = [[] for _ in range(n)]
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            map[idx].append(i)
        dist = [-1]*n
        for i in range(n):
            if len(map[i]) == 2:
                dist[i] = map[i][1] - map[i][0] - 1

        for i in range(n):
            if dist[i] != -1:
                if dist[i] != distance[i]:
                    return False
        return True

s = "abaccb"
distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
ans = Solution().checkDistances(s, distance)
print(ans)
