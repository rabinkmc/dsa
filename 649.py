"""
There are two things a senator can do

1. Pick the nearest senator to remove
2. Check if there exists only 

RDD

1. RDD -> DDR -> DR
2. DR -> RD -> D
"""
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # first D moves to the back and removes first R
        # first R moves to the back and removes first D
        senates = deque(senate)
        while senates:
            cur = senates.popleft()
            opposition = "R" if cur == "D" else "D"
            if opposition not in senates:
                return "Radiant" if cur == "R" else "Dire"
            del senates[senates.index(opposition)]
            senates.append(cur)

        return ""


print(Solution().predictPartyVictory("RD"))
