from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        tickets_queue = deque()
        for i in range(n):
            tickets_queue.append((i, tickets[i]))

        while True:
            i, ticket = tickets_queue.popleft()
            ticket -= 1
            if i == k and ticket == 0:
                return time + 1
            if ticket != 0:
                tickets_queue.append((i, ticket))
            time += 1


tickets = [2, 3, 2]
k = 2
tickets = [5, 1, 1, 1]
k = 0
print(Solution().timeRequiredToBuy(tickets, k))
