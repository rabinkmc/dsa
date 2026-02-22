from typing import List


class Clock:
    def __init__(self, event):
        t11, t12 = [int(x) for x in event[0].split(":")]
        self.start = t11 * 60 + t12
        t11, t12 = [int(x) for x in event[1].split(":")]
        self.end = t11 * 60 + t12
        if self.end < self.start:
            self.end += 2400

    def __str__(self):
        return f"{self.start}->{self.end}"


def intersection(c1, c2):
    return c1.start <= c2.start <= c1.end


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        c1 = Clock(event1)
        c2 = Clock(event2)
        return intersection(c1, c2) or intersection(c2, c1)


event1 = ["10:00", "1:00"]
event2 = ["11:00", "12:00"]
ans = Solution().haveConflict(event1, event2)
print(ans)
