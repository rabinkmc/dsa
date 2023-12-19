"""
There are two things a senator can do

1. Pick the nearest senator to remove
2. Check if there exists only 

RDD

1. RDD -> DDR -> DR
2. DR -> RD -> D

better approach
1. maintain two queues r and d
2. pop the first element from each queue, check the priority,
   the one with higher priority gets appended at the end of its
   respective queue with updated priority
"""
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        for i, party in enumerate(senate):
            if party == "R":
                r.append(i)
            else:
                d.append(i)
        n = len(senate)
        while r and d:
            rcur, dcur = r.popleft(), d.popleft()
            if rcur < dcur:
                r.append(rcur + n)
            else:
                d.append(dcur + n)

        return "Radiant" if r else "Dire"


print(Solution().predictPartyVictory("RRRRRDDDDDD"))
