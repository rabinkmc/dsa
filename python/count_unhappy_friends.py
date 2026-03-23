from typing import List

"""
However, this pairing may cause some of the friends to be unhappy. 
A friend x is unhappy if x is paired with y and there exists a 
friend u who is paired with v but:

    x prefers u over y, and
    u prefers x over v.
"""


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        ans = 0
        prefs = [[0] * n for _ in range(n)]
        friend_map = {}
        for x, y in pairs:
            friend_map[x] = y
            friend_map[y] = x
        for x in range(n):
            for pos in range(len(preferences[x])):
                y = preferences[x][pos]
                prefs[x][y] = pos
        for x in range(n):
            y = friend_map[x]
            rank_of_y = prefs[x][y]
            for u_rank in range(rank_of_y):
                u = preferences[x][u_rank]
                v = friend_map[u]
                if prefs[u][x] < prefs[u][v]:
                    ans += 1
                    break
        return ans


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
ans = Solution().unhappyFriends(n, preferences, pairs)
print(ans)
