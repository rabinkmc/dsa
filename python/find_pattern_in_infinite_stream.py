# Definition for an infinite stream.
# class InfiniteStream:
#     def next(self) -> int:
#         pass
from collections import deque


class Solution:
    def findPattern(
        self, stream: Optional["InfiniteStream"], pattern: List[int]
    ) -> int:
        m = len(pattern)
        P = 5
        MOD = 1000_000_007
        highest_pow = pow(P, m - 1, MOD)
        p_hash = 0
        t_hash = 0
        last_val = 0
        q = deque()
        for i in range(m):
            p_hash = (p_hash * P + pattern[i]) % MOD
            new_val = stream.next()
            t_hash = (t_hash * P + new_val) % MOD
            q.append(new_val)
        found = False
        i = 0
        while True:
            if p_hash == t_hash:
                return i
            last_val = q.popleft()
            t_hash = (t_hash - last_val * highest_pow) % MOD
            new_val = stream.next()
            q.append(new_val)
            t_hash = (t_hash * P + new_val) % MOD
            i += 1
